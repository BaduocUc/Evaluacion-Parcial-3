from django.shortcuts import render # type: ignore
from .models import Category, Product, Foundation

# Create your views here.

def index(request):
    Productos = Product.objects.all()  
    context = {"Productos":Productos}
    return render(request, 'appShop/index.html', context)
