from django.contrib import admin
from django.urls import path, include
import books.views

urlpatterns = [
    path('', books.views.index, name="show_book_route"),
    path('create', books.views.create_book),
    path('update/<book_id>', books.views.update_book, name='update_book_route')
]
