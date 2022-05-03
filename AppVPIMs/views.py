from django.shortcuts import render

def inicio(request):
    return render(request, "AppVPIMs/inicio.html")

def guitarras(request):
    return render(request, "AppVPIMs/guitarras.html")

def bajos(request):
    return render(request, "AppVPIMs/bajos.html")

def pedales(request):
    return render(request, "AppVPIMs/pedales.html")

def amplificadores(request):
    return render(request, "AppVPIMs/amplificadores.html")
