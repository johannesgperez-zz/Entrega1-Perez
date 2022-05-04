from django.http import HttpResponse
from django.shortcuts import render

from AppVPIMs.forms import GuitarraFormulario, BajoFormulario, PedalFormulario, AmpliFormulario
from AppVPIMs.models import Amplificador, Bajo, Guitarra, Pedal

def inicio(request):
    return render(request, "AppVPIMs/inicio.html")

def guitarras(request):
    guitarras = Guitarra.objects.all()
    return render(request, "AppVPIMs/guitarras.html", {'guitarras':guitarras})

def bajos(request):
    bajos = Bajo.objects.all()
    return render(request, "AppVPIMs/bajos.html", {'bajos':bajos})

def pedales(request):
    pedales = Pedal.objects.all()
    return render(request, "AppVPIMs/pedales.html", {'pedales':pedales})

def amplificadores(request):
    amplificadores = Amplificador.objects.all()
    return render(request, "AppVPIMs/amplificadores.html", {'amplificadores':amplificadores})

def guitarra_formulario(request):
    if request.method == 'POST':
        miFormulario = GuitarraFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            guitarra = Guitarra(marca=informacion['marca'], 
                            modelo=informacion['modelo'], 
                            anio=informacion['anio'], 
                            cuerdas=informacion['cuerdas'], 
                            descripcion=informacion['descripcion'], 
                            precio=informacion['precio'], 
                            telefono_contacto=informacion['telefono_contacto'])
            guitarra.save()
            return render(request, "AppVPIMs/inicio.html")
    else:
        miFormulario = GuitarraFormulario()
    return render(request, "AppVPIMs/guitarra_formulario.html", {"miFormulario":miFormulario})

def bajo_formulario(request):
    if request.method == 'POST':
        miFormulario = BajoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            bajo = Bajo(marca=informacion['marca'], 
                            modelo=informacion['modelo'], 
                            anio=informacion['anio'], 
                            cuerdas=informacion['cuerdas'], 
                            descripcion=informacion['descripcion'], 
                            precio=informacion['precio'], 
                            telefono_contacto=informacion['telefono_contacto'])
            bajo.save()
            return render(request, "AppVPIMs/inicio.html")
    else:
        miFormulario = BajoFormulario()
    return render(request, "AppVPIMs/bajo_formulario.html", {"miFormulario":miFormulario})

def pedal_formulario(request):
    if request.method == 'POST':
        miFormulario = PedalFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            pedal = Pedal(marca=informacion['marca'], 
                            tipo_efecto=informacion['tipo_efecto'], 
                            anio=informacion['anio'], 
                            descripcion=informacion['descripcion'], 
                            precio=informacion['precio'], 
                            telefono_contacto=informacion['telefono_contacto'])
            pedal.save()
            return render(request, "AppVPIMs/inicio.html")
    else:
        miFormulario = PedalFormulario()
    return render(request, "AppVPIMs/pedal_formulario.html", {"miFormulario":miFormulario})

def ampli_formulario(request):
    if request.method == 'POST':
        miFormulario = AmpliFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            ampli = Amplificador(marca=informacion['marca'], 
                            tipo_amplificador=informacion['tipo_amplificador'], 
                            anio=informacion['anio'], 
                            descripcion=informacion['descripcion'], 
                            precio=informacion['precio'], 
                            telefono_contacto=informacion['telefono_contacto'])
            ampli.save()
            return render(request, "AppVPIMs/inicio.html")
    else:
        miFormulario = AmpliFormulario()
    return render(request, "AppVPIMs/ampli_formulario.html", {"miFormulario":miFormulario})

def busqueda_instrumento(request):
    return render(request, "AppVPIMs/busqueda_instrumento.html")

def buscar(request):
    if request.GET["marca"]:
        marca = request.GET['marca']
        guitarras = Guitarra.objects.filter(marca__icontains=marca)
        bajos = Bajo.objects.filter(marca__icontains=marca)
        pedales = Pedal.objects.filter(marca__icontains=marca)
        amplificadores = Amplificador.objects.filter(marca__icontains=marca)
        return render(request, "AppVPIMs/resultadosBusqueda.html", {"guitarras":guitarras, "bajos":bajos, "pedales":pedales, "amplificadores":amplificadores, "marca":marca})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
