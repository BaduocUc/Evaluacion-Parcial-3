from django.contrib import admin # type: ignore
from .models import Category, Product, Foundation, Contacto

class ProductAdmin(admin.ModelAdmin):
    list_display = ["products","price","id_category"]
    list_editable = ["price"]
    search_fields = ["products","price","id_category"]
    list_filter = ["id_category"]
    list_per_page = 5

# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Foundation)
admin.site.register(Contacto)



