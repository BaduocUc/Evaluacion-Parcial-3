from django import forms # type: ignore
from .models import Contacto, Product, Foundation
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import User # type: ignore

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
        
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']