from django.urls import path
from AppVPIMs import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('guitarras', views.guitarras, name="guitarras"),
    path('bajos', views.bajos, name="bajos"),
    path('pedales', views.pedales, name="pedales"),
    path('amplificadores', views.amplificadores, name="amplificadores"),
    path('guitarraformulario', views.guitarra_formulario, name="guitarraformulario"),
    path('bajoformulario', views.bajo_formulario, name="bajoformulario"),
    path('pedalformulario', views.pedal_formulario, name="pedalformulario"),
    path('ampliformulario', views.ampli_formulario, name="ampliformulario"),
    path('busquedaguitarra', views.busqueda_guitarra, name="busquedaguitarra"),
    path('resultadosBusquedaG/', views.buscar)
]
