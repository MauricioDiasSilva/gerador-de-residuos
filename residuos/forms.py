# residuos/forms.py
from django import forms
from .models import Residuo, Coleta

class ResiduoForm(forms.ModelForm):
    class Meta:
        model = Residuo
        fields = ['tipo', 'quantidade']

class ColetaForm(forms.ModelForm):
    class Meta:
        model = Coleta
        fields = ['residuo', 'data_coleta', 'localizacao']
