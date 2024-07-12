from django import forms # type: ignore
from .models import Contacto, Product, Foundation

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        
class FundacionForm(forms.ModelForm):
    
    class Meta:
        model = Foundation
        fields = '__all__'