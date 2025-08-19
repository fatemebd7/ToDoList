from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Registration successful. You can login now.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("task_list")
    else:
        form = UserLoginForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
