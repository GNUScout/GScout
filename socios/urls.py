#from django.conf.urls import patterns
from django.conf.urls.defaults import patterns
from socios.views import *
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
   (r'^$',socios_main_page),  
   ('^new/',login_required(TemplateView.as_view(template_name='socios/f_asociado.html'))),
   ('^search/',login_required(TemplateView.as_view(template_name='socios/search.html'))),
   (r'^create_personal/', newPersonal),
   (r'^search_socio/', search),
   (r'([0-9]+)/personales/?', personales_socio),
   (r'([0-9]+)/economicos/?', economicos_socio),
   (r'([0-9]+)/medicos/?', medicos_socio),
   (r'([0-9]+)/familiares/?', familiares_socio),
   (r'([0-9]+)/edit_personales/?', edit_personales),
   (r'^modify_personales/?', modify_personales),
   (r'([0-9]+)/edit_economicos/?', edit_economicos),
   (r'^modify_economicos/?', modify_economicos),
   (r'([0-9]+)/edit_medicos/?', edit_medicos),
   (r'^modify_medicos/?', modify_medicos),
   (r'^listado/', listado),
   (r'^listado_del/', listado_del),
   (r'^listado_economicos/', listado_economicos),
   (r'^del_socios/', del_socios),
   #(r'^export_economicos/?', export_economicos),
   #(r'^export/?', export),
   ('^familiares/',login_required(TemplateView.as_view(template_name='socios/f_familiares.html'))),
   (r'search_familia', search_familia),
   (r'([A-Z]?[0-9]+\-?[a-z]?[A-Z]?)/edit_familia/?', edit_familia),
   (r'modify_familia/?', modify_familia),
   (r'post_change_familia/?', post_change_familia),
   (r'([0-9]+)/change_familia/?', change_familia),
   (r'cambio_unidad/?', cambio_unidad),  
)
