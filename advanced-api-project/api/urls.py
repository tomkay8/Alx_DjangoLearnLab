from django.urls import path
from .views import BookListCreateView, BookDetailView, ListView, UpdateView, DeleteView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path('list/', ListView.as_view(), name='list-view'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update-view'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete-view'),
]

