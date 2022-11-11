from .models import User, Profile
from django.shortcuts import render, redirect
from accounts.forms import SignupForm, UpdateForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm 
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model



# Create your views here.

def index(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)

def signup(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:index")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "accounts:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("accounts:index")

@login_required
def update(request):
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = UpdateForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts:update")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/password.html", context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("reviews:index")

def mypage(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/mypage.html", context)

def profile(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/profile.html", context)

@login_required
def follow(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.user == user:
        return redirect('accounts:mypage',pk)

    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect('accounts:mypage',pk)
