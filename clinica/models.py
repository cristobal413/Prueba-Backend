from django.db import models
class Producto(models.Model):
    nombre_mascota = models.CharField(max_length=100, verbose_name='Nombre Mascota')
    nombre_dueno = models.CharField(max_length=150, verbose_name='Nombre Dueño')
    numero_chip = models.CharField(max_length=15, unique=True, verbose_name="identificador unico")
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    edad_anios = models.IntegerField()
    en_tratamiento = models.BooleanField(default=True)
    fecha_registro = models.DateField(auto_now_add=True)
    
   
