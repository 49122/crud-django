from django.contrib import admin

from bedu_travels.models import *

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("nombre","direccion","precio",)
    
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'numero_celular', 'folio',)
    
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'precio', 'iva',)
    
    
@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'hotel', 'numero_habitacion', 'folio_reservacion',)
    

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('reservacion', 'numero_orden',)