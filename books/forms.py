from django import forms
from .models import Book, Genre, Author
from cloudinary.forms import CloudinaryJsFileField


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'desc', 'price', 'version', 'genre')
    cover = CloudinaryJsFileField()

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False)