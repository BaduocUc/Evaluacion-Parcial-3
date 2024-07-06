from django.contrib import admin # type: ignore
from .models import Category, Product, Foundation

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Foundation)


