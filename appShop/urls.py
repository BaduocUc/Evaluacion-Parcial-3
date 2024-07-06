#from django.conf.urls import url
from django.urls import path # type: ignore
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('tienda/', tienda, name='tienda')
]
