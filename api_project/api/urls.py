# api/urls.py
from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the simple BookList view
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes from the router (CRUD)
    path('', include(router.urls)),
]

