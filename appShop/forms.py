from django import forms # type: ignore
from .models import Contacto

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'