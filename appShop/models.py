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
    price            = models.IntegerField(blank=True, null=True) 
    id_category      = models.ForeignKey('Category',on_delete=models.CASCADE, db_column='idCategory')
    image            = models.ImageField(upload_to="productos", null=True)
    description      = models.TextField()  
    activo           = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.products)

    
class Foundation(models.Model):
    id_foundation    = models.AutoField(db_column='idFoundation', primary_key=True)
    foundations      = models.CharField(max_length=50, blank=True, null=True) 
    image            = models.ImageField(upload_to="fundaciones", null=True)
    description      = models.TextField()
    link             = models.URLField(max_length = 200)  
    activo           = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.foundations)

op_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre          = models.CharField(max_length=50)
    correo          = models.EmailField()
    tipo_consulta   = models.IntegerField(choices=op_consultas)
    mensaje         = models.TextField()
    avisos          = models.BooleanField()
    
    def __str__(self):
        return str(self.nombre)
    
    

