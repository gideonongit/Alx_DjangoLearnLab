from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "blog/home.html", {"posts": posts})

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm

def register(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "auth/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "auth/profile.html", {"form": form})


"ListView", "DetailView", "CreateView", "UpdateView", "DeleteView"
