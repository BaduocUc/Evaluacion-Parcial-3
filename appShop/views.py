from django.shortcuts import render # type: ignore
from .models import Category, Product, Foundation

# Create your views here.

def home(request):   
    return render(request, 'appShop/home.html')

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

def nosotros(request):
    return render(request, 'appShop/nosotros.html')

def donaciones(request):
    fundaciones = Foundation.objects.filter(activo=True)
    
    context = {
        'Fundaciones': fundaciones
    }
    
    return render(request, 'appShop/donaciones.html', context)

def contacto(request):
    return render(request, 'appShop/contacto.html')

def crudFundacion(request):
    fundacion = Foundation.objects.all()
    context = {'fundacion': fundacion}
    return render(request, 'appShop/CRUD/Foundation/list.html', context)

def crudProduct(request):
    producto = Product.objects.all()
    context = {'producto': producto}
    return render(request, 'appShop/CRUD/Product/list.html', context)
    

