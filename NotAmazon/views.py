from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

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

def logIn(request):
    return render(request, "logIn.html", {})

def signUp(request):
    return render(request, "signUp.html", {})