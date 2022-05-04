from django.urls import path
from AppVPIMs import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('guitarras', views.guitarras, name="guitarras"),
    path('bajos', views.bajos, name="bajos"),
    path('pedales', views.pedales, name="pedales"),
    path('amplificadores', views.amplificadores, name="amplificadores"),
    path('guitarraFormulario', views.guitarra_formulario, name="guitarraFormulario"),
    path('bajoFormulario', views.bajo_formulario, name="bajoFormulario"),
    path('pedalFormulario', views.pedal_formulario, name="pedalFormulario"),
    path('ampliFormulario', views.ampli_formulario, name="ampliFormulario"),
    path('busquedaInstrumento', views.busqueda_instrumento, name="busquedaInstrumento"),
    path('resultadosBusqueda/', views.buscar)
]
