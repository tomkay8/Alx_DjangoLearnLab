from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# List all books and create a new book
# BookListCreateView handles:
# - GET (list all books)
# - POST (create new book if authenticated)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can create
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Retrieve, update, delete a single book
# BookDetailView handles:
# - GET (single book detail)
# - PUT/PATCH (update book if authenticated)
# - DELETE (delete book if authenticated)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
