from .models import User, Profile
from django.shortcuts import render, redirect
from accounts.forms import SignupForm, UpdateForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm 
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse



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
            return redirect("/")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "/")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("/")

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
    if request.user.is_authenticated:
            User = get_user_model()
            me = request.user
            you = User.objects.get(pk=pk)
            if me != you:
                if you.followers.filter(pk=me.pk).exists():
                    you.followers.remove(me)
                    is_followed =False
                else :
                    you.followers.add(me)
                    is_followed = True
                context ={
                    'is_followed' : is_followed,
                    'followers_count' :  you.followers.count(),
                    'followings_count' : you.followings.count(),
                }
                return JsonResponse(context)
            return redirect('accounts:mypage', you.username)
    return redirect('accounts:login')
