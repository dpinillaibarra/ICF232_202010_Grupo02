# cursos/urls.py
from django.conf.urls import url, re_path
from django.urls import path,include
from cursos import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', views.HomePageView.as_view(), name="index"),
	url(r'cursos/', views.HomeCursosView.as_view(), name="cursos"),
	url(r'^curso/upload/', views.Modelo_Form_Upload, name="upload"),
	url(r'^curso/rubrica/', views.Modelo_Form_Rubrica, name="rubrica"),
	re_path(r'^curso/(?P<sigla>ICF[0-9]{3})/$', views.DetalleCursoView.as_view(),name="detalle"),
	path('accounts/', include('accounts.urls')),
	path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
