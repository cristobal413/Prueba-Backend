from django.contrib import admin
from .models import Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_clasificacion', 'activa', 'total_pacientes_asociados')
    list_filter = ('activa', 'codigo_clasificacion')
    search_fields = ('nombre','codigo_clasificacion')
  