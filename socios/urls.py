# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from socios.views import *

urlpatterns = patterns('',
   ('^new/', 'django.views.generic.simple.direct_to_template',
     {'template': 'socios/f_asociado.html'}),
   ('^search/', 'django.views.generic.simple.direct_to_template',
     {'template': 'socios/search.html'}),                    
   (r'^create_personal/', newPersonal),
   (r'^search_socio/', search),
   ('^prueba/', 'django.views.generic.simple.direct_to_template',
     {'template': 'socios/f_medicos.html'}),
)

