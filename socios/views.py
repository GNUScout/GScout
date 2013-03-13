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
    
    return HttpResponseRedirect('/')
