from django.db import models

class Guitarra(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()
    cuerdas = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Bajo(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    anio = models.IntegerField()
    cuerdas = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Pedal(models.Model):
    marca = models.CharField(max_length=40)
    tipo_efecto = models.CharField(max_length=40)
    anio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Amplificador(models.Model):
    marca = models.CharField(max_length=40)
    tipo_amplificador = models.CharField(max_length=40)
    anio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)


# class Product(models.Model):
#     item= models.CharField(max_length=200)
#     price= models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return str(self.item) + ": $" + str(self.price)
