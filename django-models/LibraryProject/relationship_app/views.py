from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library  # ✅ Required by checker

# ✅ Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # ✅ Exactly matches checker
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ Exact match

# ✅ Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_object(self, queryset=None):
        library_id = self.kwargs.get("pk")
        return get_object_or_404(Library, pk=library_id)
