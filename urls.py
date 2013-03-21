import os
from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^accounts/', include('gaeauth.urls')),
    ('^$', 'empleados.views.index'),
    
    (r'^prueba/', 'plus.views.index'),
    (r'^oauth2callback', 'plus.views.auth_return'),
    (r'^socios/', include('socios.urls')),
    ('^otra/', 'django.views.generic.simple.direct_to_template',
     {'template': 'socios/prueba.html'}),  

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    #(r'^accounts/login/$', 'django.contrib.auth.views.login',
    #                    {'template_name': 'plus/login.html'}),

    #(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': os.path.join(os.path.dirname(__file__), 'static')
#}),
                       
    
)
