# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from socios.views import *

urlpatterns = patterns('',
   ('^personales/', 'django.views.generic.simple.direct_to_template',
     {'template': 'socios/f_asociado.html'}),
   (r'^create_personal/', newPersonal),
   ('^prueba/', 'django.views.generic.simple.direct_to_template',
     {'template': 'socios/f_medicos.html'}),
)

