from django.contrib import admin # type: ignore
from .models import Category, Product, Foundation, Contacto

class ProductAdmin(admin.ModelAdmin):
    list_display = ["products","price","id_category","activo"]
    list_editable = ["price","activo"]
    search_fields = ["products","price","id_category"]
    list_filter = ["id_category"]
    list_per_page = 5
    
class FoundationAdmin(admin.ModelAdmin):
    list_display = ["foundations","link","activo"]
    list_editable = ["link","activo"]
    search_fields = ["foundations","activo"]
    list_filter = ["activo"]
    list_per_page = 5

# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Foundation, FoundationAdmin)
admin.site.register(Contacto)



