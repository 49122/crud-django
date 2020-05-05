from django.db import models


class Hotel(models.Model):    
    nombre = models.CharField(max_length=50)
    direccion = models.TextField(max_length=100)
    precio = models.IntegerField()
    
    def __str__(self):
        return "{} - {}".format(self.nombre, self.precio)
    
    class Meta:
        verbose_name_plural = 'Hoteles'


class Persona(models.Model): 
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    numero_celular = models.CharField(max_length=10)
    
    def __str__(yyself):
        return "{} - {}". format(self.nombre, self.numero_celular)


class Cliente(Persona):
    folio = models.CharField(max_length=10)
    
    def __str__(self):
        return "{} - {}". format(self.folio, self.nombre)
    

class Producto(models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    iva = models.FloatField(default=0.16)
        
    def __str__(self):
        return "{} - {}". format(self.descripcion, self.precio)
    
    
class Reservacion(models.Model):    
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    numero_habitacion = models.IntegerField()
    folio_reservacion = models.CharField(max_length=10)

    def __str__(self):
        return "{} - {} - {}". format(self.folio_reservacion, self.numero_habitacion, self.cliente)
    
    class Meta:
        verbose_name_plural = 'Reservaciones'


    
class Orden(models.Model):
    reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    numero_orden = models.IntegerField()
    
    def subtotal(self):
        subtotal = 0
        for producto in self.productos:
            subtotal += producto.precio
        return subtotal

    def __str__(self):
        return "{} - {}". format(self.numero_orden, self.reservacion)
    
    class Meta:
        verbose_name_plural = 'Ordenes'

