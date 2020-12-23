from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Genre
from .forms import BookForm, SearchForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.


def index(request):
    books = Book.objects.all()

    # when a search query is submitted
    if request.GET:
        # always true query:
        queries = ~Q(pk__in=[])

        # if a title is specified, add it to the query
        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            queries = queries & Q(title__icontains=title)

        # if a genre is specified, add it to the query
        if 'genre' in request.GET and request.GET['genre']:
            print("adding genre")
            genre = request.GET['genre']
            queries = queries & Q(genre__in=genre)

        # update the existing book found
        books = books.filter(queries)

    genres = Genre.objects.all()
    search_form = SearchForm(request.GET)
    return render(request, 'books/index.template.html', {
        'books': books,
        'search_form': search_form
    })


@login_required
def create_book(request):
    if request.method == 'POST':
        create_form = BookForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            messages.success(
                request, f"New book {create_form.cleaned_data['title']} has been created")
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
            messages.success(
                request, f"Book {book_form.cleaned_data['title']} has been updated")
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
