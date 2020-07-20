from django import forms
from .models import Documento, Rubrica

class DocumentoForma(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ('titulo',
                  'documento',
                  'comentario')

class RubricaForma(forms.ModelForm):
    class Meta:
        model = Rubrica
        fields = ('titulo',
                  'rubrica')