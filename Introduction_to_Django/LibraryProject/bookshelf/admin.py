from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # fields to show in list view
    search_fields = ('title', 'author')                     # enables search by these fields
    list_filter = ('publication_year',)                     # adds a filter sidebar
