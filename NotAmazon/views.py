from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Item

# Creating a Register form class
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields = ["username", "email", "password1", "password2"]

# Create your views here.
def index(request):
    context={}
    context["Title"] = "Thou Not Amazon"    
    return render(request, "home.html", context)

def products(request):
    return render(request, "products.html", {})

def shop(request):
    item_list = Item.objects.all()

    context = {"item_list": item_list}
    return render(request, "shop.html", context)

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password2 = request.POST["password"]

        user = authenticate(request, username=username, password=password2)

        if user is not None:
            form = login(request, user)

            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "user_login.html", {"form":form})

def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()

    return render(request, "user_register.html", {"form":form})

#def signUp(request):
#    return render(request, "signUp.html", {})