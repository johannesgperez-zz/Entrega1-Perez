from django import forms

class GuitarraFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    anio = forms.IntegerField()
    cuerdas = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    telefono_contacto = forms.IntegerField()

class BajoFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    anio = forms.IntegerField()
    cuerdas = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    telefono_contacto = forms.IntegerField()

class PedalFormulario(forms.Form):
    marca = forms.CharField()
    tipo_efecto = forms.CharField()
    anio = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    telefono_contacto = forms.IntegerField()

class AmpliFormulario(forms.Form):
    marca = forms.CharField()
    tipo_amplificador = forms.CharField()
    anio = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    telefono_contacto = forms.IntegerField()

