from django.conf.urls import *
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('univalle.home.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    
    # vistas del reset del password
    url(r'^reset/password_reset', password_reset,{'template_name':'RecuperarPassword/password_reset_form.html', 
        'email_template_name':'RecuperarPassword/password_reset_email.html'}, 
        name = 'password_reset'),
        
    url(r'^reset/password_msj_done', password_reset_done,{'template_name':'RecuperarPassword/password_msj_done.html'},
        name = 'password_reset_done'),
        
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,{'template_name':'RecuperarPassword/password_reset_confirm.html'},
        name = 'password_reset_confirm'),
       
    url(r'^reset/done', password_reset_complete, {'template_name': 'RecuperarPassword/password_reset_complete.html'},
        name = 'password_reset_complete'),
        
       
)
