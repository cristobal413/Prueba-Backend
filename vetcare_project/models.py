from django.db import models
class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Canino, Felino, Ave Psitacida')
    codigo_clasificacion = models.CharField(max_length=10, unique=True, verbose_name='ESP-CAN, ESP-FEL, ESP-AVE')
    descripcion = models.TextField(blank=True, null=True)
    activa = models.BooleanField(default=True)
   
    def __str__(self):
        return f'{self.nombre} - {self.codigo_clasificacion}'
    class Meta:
        verbose_name = 'Especie_Mascotas'
        verbose_name_plural = 'Especie'
        ordering = ['-fecha_ingreso']