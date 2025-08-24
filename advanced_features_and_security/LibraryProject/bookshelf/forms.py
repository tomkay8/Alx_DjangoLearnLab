from django import forms

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

