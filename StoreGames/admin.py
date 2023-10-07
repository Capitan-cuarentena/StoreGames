from django.contrib import admin
from .models import Usuario
from .models import Producto
from .models import Carrito
# Register your models here.
admin.site.register(Usuario)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombreProducto', 'precioProducto', 'stockProd', 'imagen']

@admin.register(Carrito)
class ventas(admin.ModelAdmin):
    list_display = ['usuario', 'producto', 'cantidad']

