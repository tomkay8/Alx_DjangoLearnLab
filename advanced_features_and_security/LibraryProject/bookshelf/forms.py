from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    q = forms.CharField(
        label="Search",
        max_length=100,
        required=False,
        strip=True,
    )

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # adjust to match your Book model fields
