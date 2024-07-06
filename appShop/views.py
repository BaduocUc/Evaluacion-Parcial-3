from django.shortcuts import render # type: ignore
from .models import Category, Product, Foundation

# Create your views here.

def index(request):
    Productos = Product.objects.all()  
    context = {"Productos":Productos}
    return render(request, 'appShop/index.html', context)

def tienda(request):
    categorias_seleccionadas = request.GET.getlist('categoria')
    if categorias_seleccionadas:
        productos = Product.objects.filter(id_category__category__in=categorias_seleccionadas)
    else:
        productos = Product.objects.all()
    
    categorias = Category.objects.all()
    
    context = {
        'Productos': productos,
        'Categorias': categorias,
        'categorias_seleccionadas': categorias_seleccionadas,
    }
    return render(request, 'appShop/tienda.html', context)


