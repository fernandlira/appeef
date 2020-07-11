from django import forms
from .models import Viaje, Conductor

class ViajeForm(forms.Form):
    conductor = forms.ModelChoiceField(queryset=Conductor.objects.all(), required=True)