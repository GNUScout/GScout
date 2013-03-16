# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template.loader import get_template
from django.template import RequestContext
from django.contrib.sessions.models import Session
from socios.models import *
from django.contrib.sessions.models import Session
import datetime  


@csrf_protect
def newPersonal(request):
    if request.POST['form_id'] == "f1":
        s_socio = request.session.get('d_socio', {})
        s_socio['socio'] = Socio(n_asociado = request.POST['n_asociado']) 
        if (Socio.objects.filter(n_asociado=s_socio['socio'].n_asociado).count() > 0):
            return render_to_response('socios/f_asociado.html',{'errorSocio': 'El Número de asociado ya existe.'}, context_instance=RequestContext(request))
        else: 
            request.session['d_socio'] = s_socio
            return render_to_response('socios/f_personales.html', context_instance=RequestContext(request))
    if request.POST['form_id'] == "f2":
        s_socio = request.session.get('d_socio', {})
        datos = D_Personales(nombre = request.POST['nombre'],
                             apellidos = request.POST['apellidos'],
                             dni = request.POST['dni'],
                             sexo = request.POST['sexo'],
                             f_nacimiento = request.POST['f_nacimiento'],
                             direccion = request.POST['direccion'],
                             c_postal = request.POST['c_postal'],
                             localidad = request.POST['localidad'],
                             provincia = request.POST['provincia'],
                             fijo = request.POST['fijo'],
                             movil = request.POST['movil'],
                             f_ingreso = datetime.datetime.now(),
                             seccion = request.POST['seccion'],
                             estudios = request.POST['estudios'],
                             profesion = request.POST['profesion'],
                             deportes = request.POST['deportes'],
                             aficiones = request.POST['aficiones'],
                             socio_id = s_socio['socio']
                             )
       # new_socio = s_socio['context']
       # datos.save()
       # new_socio.d_personales = datos
       # new_socio.save() # and saved to database
        s_socio['personales'] = datos
        request.session['d_socio'] = s_socio
        return render_to_response('socios/f_economicos.html', context_instance=RequestContext(request))
    if request.POST['form_id'] == "f3":
        s_socio = request.session.get('d_socio', {})
        datos = D_Economicos(titular = request.POST['titular'],
                             nif_titular = request.POST['nif_titular'],
                             banco = request.POST['banco'],
                             sucursal = request.POST['sucursal'],
                             localidad = request.POST['localidad'],
                             d_banco = request.POST['d_banco'],
                             d_sucursal = request.POST['d_sucursal'],
                             dc = request.POST['dc'],
                             n_cuenta = request.POST['n_cuenta'],
                             socio_id = s_socio['socio']
                             )
        #new_socio = s_socio['context']
        #datos.save()
        #new_socio.d_economicos = datos
        #new_socio.save() # and saved to database
        s_socio['economicos'] = datos
        request.session['d_socio'] = s_socio
        return render_to_response('socios/f_medicos.html', context_instance=RequestContext(request))
    if request.POST['form_id'] == "f4":
        s_socio = request.session.get('d_socio', {})
        new_socio = s_socio['socio']
        total_medicamentos= request.POST['total_medicamentos']
        
        
        
        datos = D_Medicos(ss= request.POST['ss'],
                             smp = request.POST['smp'],
                             n_poliza = request.POST['n_poliza'],
                             enfermedad = request.POST['enfermedad'],
                             t_enfermedad = request.POST['t_enfermedad'],
                             enfermedad_cfp = request.POST['enfermedad_cfp'],
                             t_enfermedad_cfp = request.POST['t_enfermedad_cfp'],
                             operado = request.POST['operado'],
                             t_operado = request.POST['t_operado'],
                             alergia = request.POST['alergia'],
                             t_alergia = request.POST['t_alergia'],
                             otras_alergias = request.POST['otras_alergias'],
                             t_otras_alergias = request.POST['t_otras_alergias'],
                             dieta = request.POST['dieta'],
                             t_dieta = request.POST['t_dieta'],
                             toma_medicamentos = request.POST['toma_medicamentos'],
                             info_adicional = request.POST['info_adicional'],
                             socio_id = s_socio['socio']
                             )
        new_socio.save()
        s_socio['personales'].save()
        #new_socio.d_personales = s_socio['personales']
        s_socio['economicos'].save()
        #new_socio.d_economicos = s_socio['economicos']
        datos.save()
        #new_socio.d_medicos = datos
         # and saved to database
        
        if total_medicamentos > 0:
            for i in range(int(total_medicamentos)):
                medicamento = Medicamentos(nombre=request.POST['m'+str(i+1)],
                                           dosis=request.POST['md'+str(i+1)],
                                           pauta=request.POST['mp'+str(i+1)],
                                           socio_id=new_socio
                                           )
                medicamento.save()
            
        
        
        
        return HttpResponseRedirect('/')
    else:
         return HttpResponseRedirect('/')
     
def search(request):
    try:
        socio = Socio.objects.get(n_asociado = request.POST['asociado'])
    except:
        return render_to_response('socios/search.html',{'errorNoFound': 'El número de asociado no existe.'}, context_instance=RequestContext(request))
    
    return HttpResponseRedirect('/socios/'+socio.n_asociado+'/personales')

def personales_socio(request, n_asociado):
    try:
        socio = Socio.objects.get(n_asociado=n_asociado)
    except:
        return  HttpResponseRedirect('/socios/search')
    
    personales = D_Personales.objects.get(socio_id=socio)
    economicos = D_Economicos.objects.get(socio_id=socio)
    medicos = D_Medicos.objects.get(socio_id=socio)
    if medicos.toma_medicamentos == "si":
        medicamentos = Medicamentos.objects.filter(socio_id=socio)
    else:
        medicamentos = None

    if personales.f_baja is not None:
        f_baja = personales.f_baja.strftime("%d-%m-%Y")
    else:
        f_baja = "No"
    
    return render_to_response('socios/datos_personales.html', {'personales': personales, 'f_nacimiento':personales.f_nacimiento.strftime("%d-%m-%Y"),'f_ingreso':personales.f_ingreso.strftime("%d-%m-%Y"), 'f_baja': f_baja})


def medicos_socio(request, n_asociado):
    try:
        socio = Socio.objects.get(n_asociado=n_asociado)
    except:
        return  HttpResponseRedirect('/socios/search')
    
    medicos = D_Medicos.objects.get(socio_id=socio)
    if medicos.toma_medicamentos == "si":
        medicamentos = Medicamentos.objects.filter(socio_id=socio)
    else:
        medicamentos = None

    
    return render_to_response('socios/datos_medicos.html', {'medicos': medicos, 'medicamentos': medicamentos })

def economicos_socio(request, n_asociado):
    try:
        socio = Socio.objects.get(n_asociado=n_asociado)
    except:
        return  HttpResponseRedirect('/socios/search')
    
    economicos = D_Economicos.objects.get(socio_id=socio)
    
    return render_to_response('socios/datos_economicos.html', {'economicos': economicos })


def edit_personales(request, n_asociado):
    socio = Socio.objects.get(n_asociado=n_asociado)
    personales = D_Personales.objects.get(socio_id=socio)
    
    if personales.f_baja is not None:
        f_baja = personales.f_baja.strftime("%Y-%m-%d")
    else:
        f_baja = "No"
        
    return render_to_response('socios/f_edit_personales.html', {'personales': personales, 'f_nacimiento':personales.f_nacimiento.strftime("%Y-%m-%d"),'f_ingreso':personales.f_ingreso.strftime("%Y-%m-%d"), 'f_baja': f_baja}, context_instance=RequestContext(request))

def edit_economicos(request, n_asociado):
    socio = Socio.objects.get(n_asociado=n_asociado)
    economicos = D_Economicos.objects.get(socio_id=socio)
       
    return render_to_response('socios/f_edit_economicos.html', {'economicos': economicos} ,context_instance=RequestContext(request))

def edit_medicos(request, n_asociado):
    socio = Socio.objects.get(n_asociado=n_asociado)
    medicos = D_Medicos.objects.get(socio_id=socio)
       
    return render_to_response('socios/f_edit_medicos.html', {'medicos': medicos} ,context_instance=RequestContext(request))

#@csrf_protect
def modify_personales(request):
    socio = D_Personales.objects.get(socio_id= request.POST['socio'])
    socio.nombre = request.POST['nombre']
    socio.apellidos = request.POST['apellidos']
    socio.dni = request.POST['dni']
    socio.sexo = request.POST['sexo']
    socio.f_nacimiento = request.POST['f_nacimiento']
    socio.direccion = request.POST['direccion']
    socio.c_postal = request.POST['c_postal']
    socio.localidad = request.POST['localidad']
    socio.provincia = request.POST['provincia']
    socio.fijo = request.POST['fijo']
    socio.movil = request.POST['movil']
    socio.f_ingreso = request.POST['f_ingreso']
    if request.POST['f_baja'] != "":
        socio.f_baja = request.POST['f_baja']
    socio.seccion = request.POST['seccion']
    socio.estudios = request.POST['estudios']
    socio.profesion = request.POST['profesion']
    socio.deportes = request.POST['deportes']
    socio.aficiones = request.POST['aficiones']
    
    socio.save()
                            
    
    return  HttpResponseRedirect('/socios/'+socio.socio_id.n_asociado+'/personales')

def modify_economicos(request):
    socio = D_Economicos.objects.get(socio_id= request.POST['socio'])
    socio.titular = request.POST['titular']
    socio.nif_titular = request.POST['nif_titular']
    socio.banco = request.POST['banco']
    socio.sucursal = request.POST['sucursal']
    socio.localidad = request.POST['localidad']
    socio.d_banco = request.POST['d_banco']
    socio.d_sucursal = request.POST['d_sucursal']
    socio.dc = request.POST['dc']
    socio.n_cuenta = request.POST['n_cuenta']
    
    
    socio.save()
                            
    
    return  HttpResponseRedirect('/socios/'+socio.socio_id.n_asociado+'/economicos')


        