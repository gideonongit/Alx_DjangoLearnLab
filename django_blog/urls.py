from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
]
