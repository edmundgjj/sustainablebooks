from django.shortcuts import render, HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.template.html', {
        'books':books
    })

def create_book(request):
    create_form = BookForm()
    return render(request, 'books/createbook.template.html', {
        'form':create_form
    })