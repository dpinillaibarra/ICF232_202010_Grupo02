from django import forms
from .models import MDocumento, MRubrica, Descripcion

class DocumentoForma(forms.ModelForm):
    class Meta:
        model = MDocumento
        fields = ('titulo',
                  'documento',
                  'comentario')
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class':'form-control','rows':'1','placeholder': 'Titulo del proyecto'}),
            'comentario': forms.Textarea(
                attrs={'class':'form-control','rows':'4','placeholder': 'Comentario sobre el proyecto'}),
        }

class RubricaForma(forms.ModelForm):
    class Meta:
        model = MRubrica
        fields = ('titulo',
                  'rubrica')
        widgets = {
            'titulo': forms.TextInput(
                attrs={'placeholder': 'Titulo del proyecto'}),
        }

class DescripcionForma(forms.ModelForm):
    class Meta:
        model = Descripcion
        fields = ('titulo',
                  'descripcion')
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class':'form-control','rows':'1','placeholder': 'Titulo del proyecto'}),
            'descripcion': forms.Textarea(
                attrs={'class':'form-control','rows':'4','placeholder': 'Descripción del proyecto'}),
        }

