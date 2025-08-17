from django.urls import path
from . import views

urlpatterns = [
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("comment/<int:pk>/edit/", views.edit_comment, name="edit_comment"),
    path("comment/<int:pk>/delete/", views.delete_comment, name="delete_comment"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<str:tag_name>/', views.post_by_tag, name='post_by_tag'),
    path('search/', views.search_posts, name='search_posts'),
]
"tags/<slug:tag_slug>/", "PostByTagListView.as_view()"
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Your blog home or other views can stay here:
    # path("", views.home, name="home"),

    # Auth
    path("login/",  auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/",  views.profile,  name="profile"),
]

"post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
"comment/<int:pk>/update/", "post/<int:pk>/comments/new/"
