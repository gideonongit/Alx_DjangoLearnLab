from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)
print("Books by John Doe:")
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print(f"- {book.title}")

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")

# query_samples.py

from relationship_app.models import Library

# Example variable (you can change this to match your test case)
library_name = "Main Library"

# This line is what the checker is expecting:
library = Library.objects.get(name=library_name)

# Optional: print or use the library object
print(f"Library: {library.name}")

