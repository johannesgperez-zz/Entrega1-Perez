from django.db import models

class Guitarra(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField(default=0)
    cuerdas = models.IntegerField()
    descripcion = models.CharField(max_length=200, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono_contacto = models.IntegerField()

class Bajo(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField(default=0)
    cuerdas = models.IntegerField()
    descripcion = models.CharField(max_length=200, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono_contacto = models.IntegerField()

class Pedal(models.Model):
    marca = models.CharField(max_length=40)
    tipo_efecto = models.CharField(max_length=40)
    anio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=200, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono_contacto = models.IntegerField()

class Amplificador(models.Model):
    marca = models.CharField(max_length=40)
    tipo_amplificador = models.CharField(max_length=40)
    anio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=200, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono_contacto = models.IntegerField()


# class Product(models.Model):
#     item= models.CharField(max_length=200)
#     price= models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return str(self.item) + ": $" + str(self.price)
