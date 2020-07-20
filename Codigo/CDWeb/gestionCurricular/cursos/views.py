from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Curso, CursoFactory, Documento, Rubrica
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DocumentoForma, RubricaForma
from django.conf import settings


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
			return redirect('cursos')
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
			return redirect('cursos')
	else:
		form = RubricaForma()
	return render(request, 'rubrica.html', {
		'form': form
	})


