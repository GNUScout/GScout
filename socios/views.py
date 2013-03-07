# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template.loader import get_template
from django.template import RequestContext
from django.contrib.sessions.models import Session
from socios.models import D_Personales



@csrf_protect
def newPersonal(request):
            
            datos = D_Personales(nombre = request.POST['nombre'],
                                 f_nacimiento = request.POST['f_nacimiento'],
                        )
   
            datos.save() # and saved to database
            
            return HttpResponseRedirect('/')
        
