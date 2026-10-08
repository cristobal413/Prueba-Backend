from django.contrib import admin
from .models import Producto

@admin.register(Producto)

class ProductoAdmin(admin.ModelAdmin):
                list_display = ('nombre_mascota', 'nombre_dueno', 'numero_chip', 'especie', 'peso_kg', 'en_tratamiento','evaluacion_riesgo')
                list_filter = ('en_tratamiento','especie','especie_codigo_clasificacion','fecha_registro')
                search_fields = ('nombre_mascota', 'nombre_dueno','numero_chip','especie_nombre','especie_codigo_clasificacion')
                list_editable = ('en_tratamiento')
                
                    
