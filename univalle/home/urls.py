# -*- coding: utf-8 -*-

from django.conf.urls import *
from univalle.home import views

urlpatterns = patterns('',
    url(r'^$', views.index_view,name='vista_principal'),
    #url(r'^productos/page/(?P<pagina>.*)/$', views.productos_view,name='vista_productos'),
    url(r'^about/$', views.about_view,name='vista_about'),
    url(r'^login/$', views.login_view,name='vista_login'),
    url(r'^logout/$', views.logout_view,name='vista_logout'),
    url(r'^registro/$', views.register_view,name='vista_registro'),
    url(r'^resultados/$', views.resultados_view,name='vista_resultados'),
    url(r'^inscripciones/$', views.add_inscripciones_view,name='vista_inscripciones'),
)
