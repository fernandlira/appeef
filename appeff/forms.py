from django import forms
from .models import Viaje, Conductor, Favorito

class ViajeForm(forms.Form):
    DISTRITOS = (("LIMA_CERCADO","LIMA CERCADO"),("ATE","ATE"),("BARRANCO","BARRANCO"),("LINCE","LINCE"),("MIRAFLORES","MIRAFLORES"))
    GUARDADO = (("0","NO"),("1","SI"))
    #conductor = forms.ModelChoiceField(queryset=Conductor.objects.filter(disponibilidad=0), required=True)
    distrito = forms.ChoiceField(choices=DISTRITOS, required=True)
    destino = forms.CharField(required=True)
    favorita = forms.ChoiceField(choices=GUARDADO, required=True, label="¿Guardar como favorita?")
    
    #conductor.widget.attrs.update({'class': 'form-control'})
    distrito.widget.attrs.update({'class': 'form-control'})
    destino.widget.attrs.update({'class': 'form-control'})
    favorita.widget.attrs.update({'class': 'form-control'})

class AceptarForm(forms.Form):
    precio = forms.FloatField(required=True)
    precio.widget.attrs.update({'class': 'form-control'})

class PuntuarForm(forms.Form):
    PUNTOS = ((1, "Malo"), (2, "Regular"), (3, "Neutro"), (4, "Bueno"), (5, "Excelente"))
    puntuacion = forms.ChoiceField(choices=PUNTOS, widget=forms.RadioSelect,required=True)

