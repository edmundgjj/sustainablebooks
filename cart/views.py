from django.shortcuts import render,  get_object_or_404, redirect, reverse
from django.contrib import messages
from books.models import Book


def add_to_cart(request, book_id):
    cart = request.session.get('shopping_cart', {})

    if book_id not in cart:
        book = get_object_or_404(Book, pk=book_id)
        cart[book_id] = {
            'id': book_id,
            'title': book.title,
            'price': float(book.price),
            'qty': int(1),
        }

        request.session['shopping_cart'] = cart

        messages.success(request, "Book has been added to your cart!")
        return redirect(reverse('view_cart'))
    else:
        cart[book_id]["qty"] = int(cart[book_id]["qty"]) + int(1)
        request.session['shopping_cart'] = cart
        return redirect(reverse('view_cart'))


def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })


def remove_from_cart(request, book_id):
    cart = request.session.get('shopping_cart', {})

    if book_id in cart:
        # remove it from the cart
        del cart[book_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")

    return redirect(reverse('view_cart'))


def update_quantity(request, book_id):
    cart = request.session.get('shopping_cart')
    if book_id in cart:
        cart[book_id]['qty'] = request.POST['qty']
        request.session['shopping_cart'] = cart
        messages.success(
            request, f"Quantity for {cart[book_id]['title']} has been changed")

    return redirect(reverse('view_cart'))
