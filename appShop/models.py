from django.db import models # type: ignore

# Create your models here.

class Category(models.Model):
    id_category  = models.AutoField(db_column='idCategory', primary_key=True) 
    category     = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return str(self.category)

    
    
class Product(models.Model):
    id_product       = models.AutoField(db_column='idProduct', primary_key=True)
    products         = models.CharField(max_length=20, blank=True, null=True) 
    id_category      = models.ForeignKey('Category',on_delete=models.CASCADE, db_column='idCategory')
    image            = models.ImageField(upload_to="productos", null=True)
    description      = models.CharField(max_length=150)  
    activo           = models.BooleanField(default=True)

    
class Foundation(models.Model):
    id_foundation    = models.AutoField(db_column='idFoundation', primary_key=True)
    foundations      = models.CharField(max_length=20, blank=True, null=True) 
    image            = models.ImageField(upload_to="fundaciones", null=True)
    description      = models.CharField(max_length=450)
    link             = models.CharField(max_length=50)  
    activo           = models.BooleanField(default=True)

