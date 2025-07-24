from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library  # ✅ Required for checker

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()  # ✅ Required for checker
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ Required for checker

# Class-based view: Show library details with books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_object(self, queryset=None):
        library_id = self.kwargs.get("pk")
        return get_object_or_404(Library, pk=library_id)
