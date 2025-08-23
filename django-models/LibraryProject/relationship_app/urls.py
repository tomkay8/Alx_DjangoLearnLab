from django.urls import path
from .views import list_books, LibraryDetailView, register_view, LoginView, LogoutView

urlpatterns = [
    path("books/", list_books, name="list_books"),   # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    

    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    # class-based view
]

