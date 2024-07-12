#from django.conf.urls import url
from django.urls import path # type: ignore
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('tienda/', views.tienda, name='tienda'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('donaciones/', views.donaciones, name='donaciones'),
    path('contacto/', views.contacto, name='contacto'),
    path('agregar-producto/', views.add_producto, name='add_producto'),
    path('listar-producto/', views.list_producto, name='list_producto'),
    path('modificar-producto/<id_product>/', views.modify_producto, name='modify_producto'),
    path('eliminar-producto/<id_product>/', views.delete_producto, name='delete_producto'),
    path('agregar-fundacion/', views.add_donaciones, name='add_donaciones'),
    path('listar-fundacion/', views.list_donaciones, name='list_donaciones'),
    path('modificar-fundacion/<id_foundation>/', views.modify_donaciones, name='modify_donaciones'),
    path('eliminar-fundacion/<id_foundation>/', views.delete_donaciones, name='delete_donaciones'),
    path('registro/', views.registro, name='registro'),
    
]

