from django.shortcuts import render # type: ignore

# Create your views here.

def index(request):
    context={}
    return render(request, 'appShop/index.html', context)
