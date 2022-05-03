from django.urls import path
from AppVPIMs import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('guitarras', views.guitarras, name="guitarras"),
    path('bajos', views.bajos, name="bajos"),
    path('pedales', views.pedales, name="pedales"),
    path('amplificadores', views.amplificadores, name="amplificadores"),
]
