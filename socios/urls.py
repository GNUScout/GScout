# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from socios.views import *

urlpatterns = patterns('',
   ('^personales/', 'django.views.generic.simple.direct_to_template',
     {'template': 'socios/p_personales.html'}),
   (r'^create_personal/', newPersonal),
)

