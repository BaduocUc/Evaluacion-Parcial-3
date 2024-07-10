#from django.conf.urls import url
from django.urls import path # type: ignore
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('tienda/', views.tienda, name='tienda'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('donaciones/', views.donaciones, name='donaciones'),
    path('contacto/', views.contacto, name='contacto'),
    path('crudFundacion', views.crudFundacion, name='crudFundacion'),
    path('crudProduct', views.crudProduct, name='crudProduct')
]

