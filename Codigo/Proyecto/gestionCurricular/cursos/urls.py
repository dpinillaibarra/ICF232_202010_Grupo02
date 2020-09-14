# cursos/urls.py
from django.conf.urls import url, re_path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cursos import views
from .views import nueva_descripcion, eliminar

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="index"),
    url(r'cursos/', views.HomeCursosView.as_view(), name="cursos"),
    url(r'^curso/ICF333/upload/', views.Modelo_Form_Upload, name="upload"),
    url(r'^curso/ICF333/rubrica/', views.Modelo_Form_Rubrica, name="rubrica"),
    url(r'^curso/ICF333/descripcion/', views.Modelo_Form_Descripcion, name="descripcion"),
    re_path(r'^curso/(?P<sigla>ICF[0-9]{3})/$', views.DetalleCursoView.as_view(), name="detalle"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('curso/ICF333/Proyecto', nueva_descripcion, name="proyecto"),
    path('curso/ICF333/Proyecto/eliminar/', eliminar, name="eliminar"),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 