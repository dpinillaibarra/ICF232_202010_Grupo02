# cursos/urls.py
from django.conf.urls import url, re_path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cursos import views
from django.views.static import serve
from .views import (nueva_descripcion, eliminar, home_documentos, home_calificaciones, 
                    EditarDescripcion, nueva_tarea, modificar_tarea, eliminar_tarea)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="index"),
    url(r'cursos/', views.HomeCursosView.as_view(), name="cursos"),
    url(r'^curso/ICF333/upload/', views.Modelo_Form_Upload, name="upload"),
    url(r'^curso/ICF333/rubrica/', views.Modelo_Form_Rubrica, name="rubrica"),
    url(r'^curso/ICF333/descripcion/', views.Modelo_Form_Descripcion, name="descripcion"),
    url(r'^curso/ICF333/documentos_subidos/', views.home_documentos, name="documentos_subidos"),
    url(r'^curso/ICF333/calificaciones/', views.home_calificaciones, name="calificaciones"),
    re_path(r'^curso/(?P<sigla>ICF[0-9]{3})/$', views.DetalleCursoView.as_view(), name="detalle"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('curso/ICF333/documentos_subidos/', home_documentos, name="documentos_subidos"),
    path('curso/ICF333/Proyecto/', nueva_descripcion, name="proyecto"),
    path('curso/ICF333/calificaciones/', home_calificaciones, name="calificaciones"),
    path('curso/ICF333/anadir_tarea/', nueva_tarea, name="anadir_tarea"),
    path('curso/ICF333/anadir_tarea/modificar_tarea/<id>/', modificar_tarea, name="modificar_tarea"),
    path('curso/ICF333/anadir_tarea/eliminar_tarea/<id>/', eliminar_tarea, name="eliminar_tarea"),
    path('curso/ICF333/Proyecto/eliminar/', eliminar, name="eliminar"),
    path('curso/ICF333/Proyecto/editar/', EditarDescripcion, name="editar"),
    url(r'^descargar/(?P<path>.*)$',serve, {'document_root':settings.MEDIA_ROOT}),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)