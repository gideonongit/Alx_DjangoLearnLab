from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Document

@permission_required('bookshelf.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'bookshelf/document_list.html', {'documents': documents})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_document(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    # ...edit logic here...
book_list
