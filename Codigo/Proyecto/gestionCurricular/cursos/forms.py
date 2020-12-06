from django import forms
from django.forms import ModelForm
from .models import MDocumento, MRubrica, Descripcion, Tarea, ActaFirmas

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

class TareaForma(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('nombre',
            	  'descripcion',
                  'exigencia',
                  'nota')
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class':'form-control','rows':'1','placeholder': 'Ingrese nombre de la nueva entrega'}),
            'descripcion': forms.Textarea(
                attrs={'class':'form-control','rows':'4','placeholder': 'Ingrese detalle de la nueva entrega'}),

        }

class ActaForma(forms.ModelForm):
    class Meta:
        model = ActaFirmas
        fields = ('Profesor_guia',
                  'Profesor_invitado_1',
                  'Profesor_invitado_2',
                  'Alumno',
                  'Rut_Alumno')
        widgets = {
            'Profesor_guia': forms.TextInput(
                attrs={'class':'form-control','rows':'1','placeholder': 'Ingrese su nombre'}), 
            'Profesor_invitado_1': forms.TextInput(
                attrs={'class':'form-control','rows':'1','placeholder': 'Ingrese nombre profesor invitado'}),
            'Profesor_invitado_2': forms.TextInput(
                attrs={'class':'form-control','rows':'1','placeholder': 'Ingrese nombre profesor invitado'}),
            'Alumno': forms.TextInput(
                attrs={'class':'form-control','rows':'1','placeholder': 'Ingrese nombre alumno a evaluar'}),
            'Rut_Alumno': forms.TextInput(
                attrs={'class':'form-control','rows':'1','placeholder': 'Ingrese rut de alumno a evaluar'}),             
        }
