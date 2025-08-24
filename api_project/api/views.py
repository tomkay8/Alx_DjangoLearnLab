from django.shortcuts import render
from rest_framework import generics
from bookshelf.models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ensures only logged-in users can see

class BookViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for Book model:
    - list, retrieve, create, update, delete
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # adjust if needed
