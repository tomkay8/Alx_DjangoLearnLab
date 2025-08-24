# api/serializers.py
from rest_framework import serializers
from bookshelf.models import Book  # Make sure this path matches your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # This will include all fields in the Book model

