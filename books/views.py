from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.template.html', {
        'books': books
    })


@login_required
def create_book(request):
    if request.method == 'POST':
        create_form = BookForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'books/createbook.template.html', {
                'form': create_form
            })
    else:
        create_form = BookForm()
        return render(request, 'books/createbook.template.html', {
            'form': create_form
        })


def update_book(request, book_id):
    book_being_updated = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":

        book_form = BookForm(request.POST, instance=book_being_updated)
        if book_form.is_valid():
            book_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'books/updatebook.template.html', {
                "form": book_form
            })
    else:
        book_form = BookForm(instance=book_being_updated)
        return render(request, 'books/updatebook.template.html', {
            "form": book_form
        })
