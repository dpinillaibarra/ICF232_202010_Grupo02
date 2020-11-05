import os
from django.shortcuts import render, redirect
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, TemplateView)
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Curso, CursoFactory, MDocumento, MRubrica, Descripcion, Tarea
from .forms import DocumentoForma, RubricaForma, DescripcionForma, TareaForma
from django.http import HttpResponse, Http404
from django.db.models import Avg





class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class HomeCursosView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        cursoFactory=CursoFactory()
        return render(request, 'cursos.html',{'cursos': cursoFactory.obtenerCursos()})
                        
class DetalleCursoView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        cursoFactory=CursoFactory()
        sigla=kwargs["sigla"]
        return render(request, 'curso.html', {'curso': cursoFactory.getCurso(sigla)})

def Modelo_Form_Upload(request):
    if request.method == 'POST':
        form = DocumentoForma(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/curso/ICF333/')
    else:
        form = DocumentoForma()
    return render(request, 'upload.html', {
        'form': form
    })

def Modelo_Form_Rubrica(request):
    if request.method == 'POST':
        form = RubricaForma(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/curso/ICF333/')
    else:
        form = RubricaForma()
    return render(request, 'rubrica.html', {
        'form': form
    })


def Modelo_Form_Descripcion(request):
    form = DescripcionForma()
   
    if request.method == 'POST':
        form = DescripcionForma(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/curso/ICF333/')
    else:
        form = DescripcionForma()
    return render(request, 'descripcion.html', {
        'form': form
    })

def eliminar(request):
    eliminar_desc = Descripcion.objects.last()
    eliminar_desc.delete()
    return redirect(to="proyecto")

def EditarDescripcion(request):
    desc = Descripcion.objects.last()
    data = {
        'form':DescripcionForma(instance=desc)
    }
    if request.method == 'POST':
        desc_form = DescripcionForma(data=request.POST, instance=desc)
        if desc_form.is_valid():
            desc_form.save()
            data['form'] = desc_form
    return render(request, 'descripcion.html', data)

def nueva_descripcion(request):
    nueva_desc = Descripcion.objects.last()
    data = {
        'nueva_desc':nueva_desc
    }
    return render(request, 'proyecto.html', data)

def home_documentos(request):
    context = {
        'file': MDocumento.objects.all()
    }
    return render(request, 'documentos_subidos.html', context)

def eliminar_documento(request, id):
    documento = MDocumento.objects.get(id=id)
    documento.delete()

    return redirect(to="documentos_subidos")

def nueva_tarea(request):
    data = {
        'form':TareaForma()
    }
    if request.method == 'POST':
        formulario = TareaForma(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Tarea creada correctamente"

    return render(request, 'anadir_tarea.html', data)

def home_calificaciones(request):
    tareas = Tarea.objects.all()
    average = tareas.aggregate(Avg("nota"))["nota__avg"]

    if average is None:
        average = 0

    average = round(average, 2)

    print(average)

    data = {
        'tareas':tareas,
        'average':average
    }
    return render(request, 'calificaciones.html', data)

def modificar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    data = {
        'form':TareaForma(instance=tarea)
    }
    if request.method == 'POST':
        formulario = TareaForma(data=request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario
    return render(request, 'modificar_tarea.html', data)

def eliminar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()

    return redirect(to="calificaciones")

def home_calificaciones_alumno(request):
    tareas = Tarea.objects.all()
    average = tareas.aggregate(Avg("nota"))["nota__avg"]

    if average is None:
        average = 0

    average = round(average, 2)

    data = {
        'tareas':tareas,
        'average':average
    }
    return render(request, 'calificaciones_alumno.html', data )

def descargar(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), context_type = "documento")
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response
        
    raise Http404

