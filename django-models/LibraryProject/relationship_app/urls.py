from django.urls import path
from .views import list_books, LibraryDetailView

add_book/", "edit_book/

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


from django.urls import path
from .views import login_view, logout_view, register_view

urlpatterns += [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]
views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=


from django.urls import path
from . import views

urlpatterns = [
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]


           
