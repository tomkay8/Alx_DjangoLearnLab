from django.urls import path
from .views import BookListCreateView, BookDetailView, ListView, UpdateView, DeleteView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/create/", CreateView.as_view(), name="books-create"),
    path("books/update/<int:pk>/", UpdateView.as_view(), name="books-update"),
    path("books/delete/<int:pk>/", DeleteView.as_view(), name="books-delete"),
]

