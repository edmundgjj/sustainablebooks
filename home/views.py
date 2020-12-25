from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from books.models import Book, Genre
from books.forms import BookForm, SearchForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.


def index(request):
    return render(request, 'home/index.template.html')


def about_us(request):
    return render(request, 'home/about_us.template.html')
