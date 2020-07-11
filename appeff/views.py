from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.http import require_http_methods
from .models import Conductor, Viaje
from .forms import ViajeForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request, "base-login.html", {})

def login(request):
    return render(request, "forms/signIn.html", {})

@require_http_methods(["GET", "POST"])
def EmpezarViaje(request):
    if request.method == "POST":
        form = ViajeForm(request.POST)
        if form.is_valid():
            viaje = Viaje(viajero=request.user,conductor=form.cleaned_data['conductor'],distrito=form.cleaned_data['distrito'],destino=form.cleaned_data['destino'])
            viaje.save()
            conductor = Conductor.objects.get(pk=viaje.conductor.id)
            conductor.disponibilidad = 1
            conductor.save()
            return redirect('viajes:empezar-viaje')
    else:
        form = ViajeForm
        return render(request, "viajes/empezar.html", {"form": form})

def CulminarViaje(request,id=1):
    viaje = Viaje.objects.get(pk=id)
    viaje.status=1
    print(viaje_conductor_disponibilidad)
    viaje.save()
