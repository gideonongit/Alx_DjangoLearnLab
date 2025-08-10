from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.admin_user = User.objects.create_superuser(username="adminuser", password="adminpass123")

        # Create some test books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2001)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2020)

        # Endpoints
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', args=[self.book1.id])
        self.update_url = reverse('book-update', args=[self.book1.id])
        self.delete_url = reverse('book-delete', args=[self.book1.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Book Three", "author": "Author C", "publication_year": 2021}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {"title": "Book Four", "author": "Author D", "publication_year": 2022}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Updated Book", "author": "Author A", "publication_year": 2001}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "Author A"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], "Author A")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
