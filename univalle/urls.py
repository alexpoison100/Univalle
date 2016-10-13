from django.conf.urls import *
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('univalle.home.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
