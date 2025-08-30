from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

        # Create a book for testing
        self.book = Book.objects.create(
            title="The Hobbit",
            author="Tolkien",
            publication_year=1937
        )

    def test_list_books(self):
        url = reverse("book-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "The Hobbit")

    def test_create_book(self):
        url = reverse("book-list-create")
        data = {"title": "1984", "author": "George Orwell", "publication_year": 1949}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest("id").title, "1984")

    def test_update_book(self):
        url = reverse("books-update", args=[self.book.id])
        data = {"title": "The Hobbit Updated", "author": "Tolkien", "publication_year": 1937}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "The Hobbit Updated")

    def test_delete_book(self):
        url = reverse("books-delete", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

        def test_filter_books_by_author(self):
        url = reverse("book-list-create") + "?author=Tolkien"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "The Hobbit")

    def test_search_books(self):
        url = reverse("book-list-create") + "?search=Hobbit"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "The Hobbit")

    def test_order_books_by_title(self):
        Book.objects.create(title="A Tale", author="Dickens", publication_year=1859)
        url = reverse("book-list-create") + "?ordering=title"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # First result should be "A Tale"
        self.assertEqual(response.data[0]["title"], "A Tale")

