from django.shortcuts import render, get_object_or_404, HttpResponse, reverse, redirect
from django.contrib import messages
from books.models import Book
from .models import Purchase
from django.conf import settings
import stripe
import json

from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

endpoint_secret = settings.ENDPOINT_SECRET


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})

    line_items = []
    all_book_ids = []

    if not cart:
        messages.error(request, "Cart is empty. Add items to checkout.")
        return redirect(reverse('view_cart'))

    else:

        for book_id, cart_item in cart.items():

            book_model = get_object_or_404(Book, pk=book_id)

            item = {
                "name": book_model.title,
                "amount": int(book_model.price * 100),
                "quantity": cart_item['qty'],
                "currency": 'sgd'
            }

            line_items.append(item)
            all_book_ids.append({
                'book_id': book_model.id,
                'qty': cart_item['qty']
            })

        current_site = Site.objects.get_current()
        domain = current_site.domain

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            client_reference_id=request.user.id,
            metadata={
                'all_book_ids': json.dumps(all_book_ids)
            },
            mode="payment",
            success_url=domain + reverse('checkout_success'),
            cancel_url=domain + reverse('checkout_cancelled')
        )

        return render(request, "checkout/checkout.template.html", {
            'session_id': session.id,
            'public_key': settings.STRIPE_PUBLISHABLE_KEY
        })


def checkout_success(request):
    request.session["shopping_cart"] = {}
    return redirect(reverse('show_book_route'))


def checkout_cancelled(request):
    return redirect(reverse('view_cart'))


@csrf_exempt
def payment_completed(request):
    # 1. verify that the data is actually sent by Stripe
    endpoint_secret = settings.ENDPOINT_SECRET
    payload = request.body
    # retrieve the signature
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        print("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Signature is invalid
        print("Invalid signature")
        return HttpResponse(status=400)

    # 2. process the order
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_payment(session)

    return HttpResponse(status=200)


def handle_payment(session):
    metadata = session['metadata']
    user = get_object_or_404(User, pk=session['client_reference_id'])
    all_book_ids = json.loads(metadata['all_book_ids'])
    for order_item in all_book_ids:
        book_model = get_object_or_404(Book, pk=order_item['book_id'])

        # Create the purchase model and save it manually
        purchase = Purchase()
        purchase.book = book_model
        purchase.user = user
        purchase.qty = order_item['qty']
        purchase.price = book_model.price

        # remember to save the model
        purchase.save()

    return HttpResponse(status=200)
