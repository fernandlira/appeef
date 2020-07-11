from django.urls import path, include
from .views import login, home, EmpezarViaje, CulminarViaje, AceptarViaje, listadoViajesU, PuntuarViaje, listar_viajes, listar_viajes_favoritos, EmpezarViajeFavorito
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", home, name="index"),
    #path("viajes-usuario", listadoViajesU, name="listar-viajes-usuario"),
    path("puntuar.viaje/<int:id>", PuntuarViaje, name="puntuar.viaje"),
    path('login', login, name="login"),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('empezar-viaje', EmpezarViaje, name='empezar-viaje'),
    path('empezar-viaje-favorito', EmpezarViajeFavorito, name='empezar-viaje-favorito'),
    path('aceptar-viaje/<int:id>', AceptarViaje, name='aceptar-viaje'),
    path('culminar-viaje/<int:id>', CulminarViaje, name='culminar-viaje'),
    path('listar-viaje', listar_viajes, name='listar-viaje'),
    path('listar-favoritos', listar_viajes_favoritos, name='listar-favoritos'),
]
