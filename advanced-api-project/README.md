API Endpoints
1. List & Create Books

    URL: /api/books/

    Methods:

    GET → Returns a list of all books. (No login required)

    POST → Add a new book. (Login required)

2. Retrieve, Update & Delete Book

    URL: /api/books/<id>/

    Methods:

        GET → Get details of a single book by its ID. (No login required)

        PUT/PATCH → Update book information. (Login required)

        DELETE → Remove a book. (Login required)

Authentication Rules

    Anyone can view books (GET requests).

    Only logged-in users can create, update, or delete books.
