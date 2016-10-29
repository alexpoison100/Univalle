# -*- coding: utf-8 -*-

from django.conf.urls import *
from univalle.administrador import views


urlpatterns = patterns('',
    url(r'^administrador/$', views.administrador_view,name='vista_administrador'),
    url(r'^crear_user/$', views.register_user_view,name='vista_crear_user'),
    url(r'^crear_carrera/$', views.register_carrera_view,name='vista_crear_carrera'),
    url(r'^editar_carrera/(?P<codigo>.*)/$', views.editar_carrera_view,name='vista_editar_carrera'),
    url(r'^listar_user/$', views.listar_usuario_view,name='vista_listar_user'),
    url(r'^listar_carreras/page/(?P<pagina>.*)/$', views.listar_carreras_view,name='vista_listar_carreras'),   
)
