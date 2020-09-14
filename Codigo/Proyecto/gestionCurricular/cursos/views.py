from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Curso, CursoFactory, Documento, Rubrica, Descripcion
from .forms import DocumentoForma, RubricaForma, DescripcionForma




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
"""
def Modelo_Form_Descripcion(request):
    mod_descripcion = Descripcion.objects.all()
    data = {
        'form':mod_descripcion(instancia=mod_descripcion)
    }
    return render(request, 'descripcion.html', data)
"""
def nueva_descripcion(request):
    nueva_desc = Descripcion.objects.last()
    data = {
        'nueva_desc':nueva_desc
    }
    return render(request, 'proyecto.html', data)

def eliminar(request):
    eliminar_desc = Descripcion.objects.last()
    eliminar_desc.delete()
    return redirect(to="proyecto")


"""(Agarrar ultimo objeto creado)def modificar(request):"""