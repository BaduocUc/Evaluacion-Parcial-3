from django import forms # type: ignore
from .models import Contacto, Product

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'