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
   (r'([0-9]+)/personales/?', personales_socio),
   (r'([0-9]+)/economicos/?', economicos_socio),
   (r'([0-9]+)/medicos/?', medicos_socio),
   (r'([0-9]+)/edit_personales/?', edit_personales),
   (r'^modify_personales/?', modify_personales),
   (r'([0-9]+)/edit_economicos/?', edit_economicos),
   (r'^modify_economicos/?', modify_economicos),
   (r'([0-9]+)/edit_medicos/?', edit_medicos),
   (r'^modify_medicos/?', modify_medicos),
   (r'^listado/', listado),
)

