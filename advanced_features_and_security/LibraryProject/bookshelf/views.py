from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.views.decorators.http import require_http_methods
from .models import Book
from .forms import BookSearchForm, BookForm, ExampleForm


@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    """
    Safe searching using Django forms + ORM (prevents SQL injection).
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            books = books.filter(title__icontains=q)  # parameterized by ORM
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})

@permission_required("bookshelf.can_create", raise_exception=True)
@require_http_methods(["GET", "POST"])
def book_create(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Create"})


"""
@permission_required("bookshelf.can_create", raise_exception=True)
@require_http_methods(["GET", "POST"])
def book_create(request):
    """
    Secure create view: CSRF token in template, form validation, ORM save.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(
                title=form.cleaned_data["title"],
                author=form.cleaned_data["author"],
            )
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Create"})
"""

@permission_required("bookshelf.can_edit", raise_exception=True)
@require_http_methods(["GET", "POST"])
def book_edit(request, pk):
    """
    Secure edit view: validates input and updates using ORM.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book.title = form.cleaned_data["title"]
            book.author = form.cleaned_data["author"]
            book.save()
            return redirect("book_list")
    else:
        form = BookForm(initial={"title": book.title, "author": book.author})
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Edit"})


@permission_required("bookshelf.can_delete", raise_exception=True)
@require_http_methods(["POST"])
def book_delete(request, pk):
    """
    Secure delete view: only POST with CSRF token allowed.
    """
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")

"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from django.views.decorators.http import require_http_methods
from .forms import BookSearchForm, BookForm

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # logic to create book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # logic to edit book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # logic to delete book
    pass
"""
