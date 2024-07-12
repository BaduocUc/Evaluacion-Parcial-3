from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Category, Product, Foundation
from .forms import ContactoForm, ProductoForm, FundacionForm
from django.contrib import messages # type: ignore

# Create your views here.

def home(request):   
    return render(request, 'appShop/home.html')


def tienda(request):
    categorias_seleccionadas = request.GET.getlist('categoria')
    if categorias_seleccionadas:
        productos = Product.objects.filter(id_category__category__in=categorias_seleccionadas,activo=True)
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
            messages.success(request,"Modificado Correctamente")
            return redirect(to="list_producto")
        else:
            messages.error(request,"Error al Guardar")
    else:
        formulario = ProductoForm()

    context = {
        'form': formulario,
    }
    return render(request, 'appShop/producto/agregar.html',context)


def list_producto(request):
    productos = Product.objects.all()
    context = {
        'Productos': productos,
    }
    return render(request, 'appShop/producto/listar.html',context)


def modify_producto(request, id_product):
    productos = get_object_or_404(Product,id_product=id_product)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,request.FILES,instance=productos)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            return redirect(to="list_producto")
        else:
            messages.error(request,"Error al Modificar")
    else:
        formulario = ProductoForm(instance=productos)
    context = {
        'form': formulario,
    }
    return render(request, 'appShop/producto/modificar.html',context)


def delete_producto(request, id_product):
    productos = get_object_or_404(Product,id_product=id_product)
    productos.delete()
    return redirect(to="list_producto")


def add_donaciones(request):
    if request.method == 'POST':
        formulario = FundacionForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Guardado Correctamente")
            return redirect(to="list_donaciones")
        else:
            messages.error(request,"Error al Guardar")
    else:
        formulario = FundacionForm()

    context = {
        'form': formulario,
    }
    return render(request, 'appShop/fundacion/agregar.html',context)


def list_donaciones(request):
    donaciones = Foundation.objects.all()
    context = {
        'donaciones': donaciones,
    }
    return render(request, 'appShop/fundacion/listar.html',context)


def modify_donaciones(request, id_foundation):
    donaciones = get_object_or_404(Foundation,id_foundation=id_foundation)
    if request.method == 'POST':
        formulario = FundacionForm(request.POST,request.FILES,instance=donaciones)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            return redirect(to="list_donaciones")
        else:
            messages.error(request,"Error al Modificar")
    else:
        formulario = FundacionForm(instance=donaciones)
    context = {
        'form': formulario,
    }
    return render(request, 'appShop/fundacion/modificar.html',context)


def delete_donaciones(request, id_foundation):
    donaciones = get_object_or_404(Foundation,id_foundation=id_foundation)
    donaciones.delete()
    return redirect(to="list_donaciones")
    