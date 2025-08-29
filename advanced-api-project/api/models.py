"""
The Author model stores information about authors.
The Book model links each book to its author via a ForeignKey.
"""

from django.db import models

class Author(models.Model):
    # Author has just a name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Book belongs to an author (one-to-many)
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

