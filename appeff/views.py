from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.http import require_http_methods
from .models import Conductor, Viaje
from .forms import ViajeForm, AceptarForm, PuntuarForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.db.models import Avg

# Create your views here.


def home(request):
    return render(request, "base-login.html", {})

def listadoViajesU(request):
    viajes = Viaje.objects.filter(viajero=request.user)
    return render(request, "viajes/listado.html", {'viajes': viajes})

def login(request):
    return render(request, "forms/signIn.html", {})

@require_http_methods(["GET", "POST"])
def EmpezarViaje(request):
    if request.method == "POST":
        form = ViajeForm(request.POST)
        if form.is_valid():
            viaje = Viaje(viajero=request.user,distrito=form.cleaned_data['distrito'],destino=form.cleaned_data['destino'])
            viaje.save()
            return redirect('appeff:index')
    else:
        form = ViajeForm
        return render(request, "viajes/empezar.html", {"form": form})

@require_http_methods(["GET", "POST"])
def AceptarViaje(request,id=1):
    if request.method == "POST":
        form = AceptarForm(request.POST)
        if form.is_valid():
            viaje = Viaje.objects.get(pk=id)
            viaje.conductor = Conductor.objects.get(pk=request.user.id)
            viaje.status="1"
            viaje.precio=form.cleaned_data['precio']
            viaje.save()
            conductor = Conductor.objects.get(pk=viaje.conductor.id)
            conductor.disponibilidad = 1
            conductor.save()
            return redirect('appeff:index')
    else:
        form = AceptarForm
        return render(request, "viajes/aceptar-viaje.html", {"form": form})

    

def CulminarViaje(request,id=1):
    viaje = Viaje.objects.get(pk=id)
    viaje.status="2"
    viaje.save()
    conductor = Conductor.objects.get(pk=viaje.conductor.id)
    conductor.disponibilidad = 0
    conductor.save()
    return redirect('appeff:index')

@require_http_methods(["GET", "POST"])
def PuntuarViaje(request,id=1):
    if request.method == "POST":
        form = PuntuarForm(request.POST)
        if form.is_valid():
            viaje = Viaje.objects.get(pk=id)
            viaje.puntuacion = form.cleaned_data['puntuacion']
            viaje.save()
            conductor = Conductor.objects.get(pk=viaje.conductor.id)
            viajes_terminados = Viaje.objects.filter(conductor=conductor,status='2',puntuacion__isnull=False).count()
            promedio = Viaje.objects.filter(conductor=conductor,status='2',puntuacion__isnull=False).aggregate(Avg('puntuacion'))
            #print(promedio.get('puntuacion__avg'))
            conductor.puntuacion = promedio.get('puntuacion__avg')
            conductor.save()
            return redirect('appeff:index')
    else:
        form = PuntuarForm
        return render(request, "viajes/puntuar-viaje.html", {"form": form})