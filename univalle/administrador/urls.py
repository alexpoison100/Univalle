# -*- coding: utf-8 -*-

from django.conf.urls import *
from univalle.administrador import views


urlpatterns = patterns('',
    url(r'^administrador/$', views.administrador_view,name='vista_administrador'),
    url(r'^crear_user/$', views.register_user_view,name='vista_crear_user'),
    url(r'^crear_inscripcion/$', views.register_inscripcion_view,name='vista_crear_inscripcion'),
    url(r'^crear_carrera/$', views.register_carrera_view,name='vista_crear_carrera'),
    url(r'^editar_usuario/(?P<pk>.*)/$', views.editar_usuario_view,name='vista_editar_usuario'),
    url(r'^editar_password/(?P<username>.*)/$', views.editar_password_view,name='vista_editar_password'),
    url(r'^editar_carrera/(?P<codigo>.*)/$', views.editar_carrera_view,name='vista_editar_carrera'),
    url(r'^editar_inscripciones/(?P<cedula>.*)/$', views.editar_inscripcion_view,name='vista_editar_inscripcion'),
    url(r'^listar_user/page/(?P<pagina>.*)/$', views.listar_usuario_view,name='vista_listar_user'),
    url(r'^listar_carreras/page/(?P<pagina>.*)/$', views.listar_carreras_view,name='vista_listar_carreras'),
    url(r'^listar_inscripciones/page/(?P<pagina>.*)/$', views.listar_inscripciones_view,name='vista_listar_inscripciones'), 

)
