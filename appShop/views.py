from django.shortcuts import render # type: ignore
from .models import Category, Product, Foundation
from .forms import ContactoForm, ProductoForm

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
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje = "Gracias por contactarnos  n/ Nos comunicaremos con usted a la brevedad."
        else:
            mensaje = "Error en el formulario. Por favor, corrige los errores."
    else:
        formulario = ContactoForm()
        mensaje = ""

    context = {
        'form': formulario,
        'mensaje': mensaje,
    }
    return render(request, 'appShop/contacto.html', context)

def add_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            mensaje = "Producto Guardado"
        else:
            mensaje = "Error al Guardar el Producto"
    else:
        formulario = ProductoForm()
        mensaje = ""

    context = {
        'form': formulario,
        'mensaje': mensaje,
    }
    return render(request, 'appShop/producto/agregar.html',context)