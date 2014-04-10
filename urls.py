import os
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^$', 'socios.views.index'),
    (r'^socios/', include('socios.urls')), 
    #(r'^upload/', include('upload.urls')), 

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
