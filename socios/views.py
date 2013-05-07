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


import csv

import httplib2
import pprint
import StringIO

from apiclient.discovery import build
from apiclient.http import MediaIoBaseUpload,MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

from django.contrib.auth.models import User

import re



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
        
        familia=Familiares.objects.all()
        
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
        return render_to_response('socios/f_familiares.html',{'familia': familia}, context_instance=RequestContext(request))
    if request.POST['form_id'] == "f5":
        
        s_socio = request.session.get('d_socio', {})
        
        
        if request.POST['new_family'] == "si":
            f_nombre =request.POST.getlist('fn[]')
            f_apellidos =request.POST.getlist('fa[]')
            f_nif =request.POST.getlist('fd[]')
            f_rol =request.POST.getlist('fr[]')
            f_tel =request.POST.getlist('ft[]')
            f_movil =request.POST.getlist('fm[]')
            f_email =request.POST.getlist('fe[]')
            
            new = Familia(nombre=f_nombre[0],
                          apellidos=f_apellidos[0],
                          nif=str(f_nif[0]),
                          )
            new.save()
            
            for i in range(len(f_nombre)):
                familiar = Familiares(nombre=f_nombre[i],
                                           apellidos=f_apellidos[i],
                                           nif=f_nif[i],
                                           rol=f_rol[i],
                                           telefono=f_tel[i],
                                           movil=f_movil[i],
                                           email=f_email[i],
                                           familia_id=Familia.objects.get(nif=str(f_nif[0]))
                                           )
                familiar.save()
            
            s_socio['socio'].familia_id= Familia.objects.get(nif=f_nif[0]) 
            
        else:
            s_socio['socio'].familia_id=Familia.objects.get(nif=request.POST['nif_family'])
            
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
            a_nombre =request.POST.getlist('m[]')
            a_dosis =request.POST.getlist('md[]')
            a_pauta =request.POST.getlist('mp[]')
            for i in range(len(a_nombre)):
                medicamento = Medicamentos(nombre=a_nombre[i],
                                           dosis=a_dosis[i],
                                           pauta=a_pauta[i],
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

def familiares_socio(request, n_asociado):
    try:
        socio = Socio.objects.get(n_asociado=n_asociado)
    except:
        return  HttpResponseRedirect('/socios/search')
    
    if socio.familia_id != None:
    
        familia = Familia.objects.get(nif=socio.familia_id.nif)
        
        familiares = Familiares.objects.filter(familia_id=socio.familia_id)
        
        hermanos = Socio.objects.filter(familia_id=socio.familia_id)
        
        lista = []
        
        for i in range(hermanos.count()):
            lista.extend(D_Personales.objects.filter(socio_id=hermanos[i]))
    
        return render_to_response('socios/datos_familiares.html', {'socio': socio, 'familia': familia, 'familiares': familiares, 'hermanos': lista },context_instance=RequestContext(request))
    
    else:
        return  HttpResponseRedirect('/socios/search')


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
    medicamentos = Medicamentos.objects.filter(socio_id=socio)
    n_medicamentos = medicamentos.count()
    
   
    
    return render_to_response('socios/f_edit_medicos.html', {'medicos': medicos, 'medicamentos': medicamentos, "n_medicamentos" : n_medicamentos } ,context_instance=RequestContext(request))

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

def modify_medicos(request):
    total_medicamentos= request.POST['total_medicamentos']
    
    socio = D_Medicos.objects.get(socio_id= request.POST['socio'])
    socio.ss = request.POST['ss']
    socio.smp = request.POST['smp']
    socio.n_poliza = request.POST['n_poliza']
    socio.enfermedad = request.POST['enfermedad']
    socio.t_enfermedad = request.POST['t_enfermedad']
    socio.enfermedad_cfp = request.POST['enfermedad_cfp']
    socio.t_enfermedad_cfp = request.POST['t_enfermedad_cfp']
    socio.operado = request.POST['operado']
    socio.t_operado = request.POST['t_operado']
    socio.alergia = request.POST['alergia']
    socio.t_alergia = request.POST['t_alergia']
    socio.otras_alergias = request.POST['otras_alergias']
    socio.t_otras_alergias = request.POST['t_otras_alergias']
    socio.dieta = request.POST['dieta']
    socio.t_dieta = request.POST['t_dieta']
    socio.toma_medicamentos = request.POST['toma_medicamentos']
    socio.info_adicional = request.POST['info_adicional']
    
    
    socio.save()
    
    old_medicamentos = Medicamentos.objects.filter(socio_id=request.POST['socio'])
    for j in old_medicamentos:
        j.delete()
    
    if total_medicamentos > 0:
            a_nombre =request.POST.getlist('m[]')
            a_dosis =request.POST.getlist('md[]')
            a_pauta =request.POST.getlist('mp[]')
            for i in range(len(a_nombre)):
                medicamento = Medicamentos(nombre=a_nombre[i],
                                           dosis=a_dosis[i],
                                           pauta=a_pauta[i],
                                           socio_id=socio.socio_id
                                           )
                medicamento.save()
    
    
   
    return  HttpResponseRedirect('/socios/'+socio.socio_id.n_asociado+'/medicos')

def listado(request):
    
    socios = D_Personales.objects.all()
     
    return render_to_response('socios/list.html', {'socios': socios} ,context_instance=RequestContext(request))

def listado_del(request):
    
    socios = D_Personales.objects.all()
     
    return render_to_response('socios/list_del.html', {'socios': socios} ,context_instance=RequestContext(request))

def del_socios(request):
    sel_socios =request.POST.getlist('sel_borrar[]')

    for i in range(len(sel_socios)):
        lista_medicamentos = Medicamentos.objects.filter(socio_id=sel_socios[i])
        for j in lista_medicamentos:
            j.delete()
        aux= D_Medicos.objects.get(socio_id=sel_socios[i])
        aux.delete()
        aux= D_Economicos.objects.get(socio_id=sel_socios[i])
        aux.delete()
        aux= D_Personales.objects.get(socio_id=sel_socios[i])
        aux.delete()
        aux= Socio.objects.get(n_asociado=sel_socios[i])
        aux.delete()
    
    socios = D_Personales.objects.all()
    
    return render_to_response('socios/list_del.html', {'socios': socios} ,context_instance=RequestContext(request))
            

def export(request):
    
    usuario = request.user
    storage = User.objects.get(username = usuario.username)
    
        
    credentials = storage.credential
    
    # Create an httplib2.Http object and authorize it with our credentials
    http = httplib2.Http()
    http = credentials.authorize(http)
    
    drive_service = build('drive', 'v2', http=http)
    
    socios = D_Personales.objects.values()
    lista=[]
    for i in range(len(socios)):
        selected=False
        if (
            (re.match(r'.*'+str(request.POST['filter0'])+'\.*',str(socios[i]['id']),re.IGNORECASE)) and
            (re.match(r'.*'+str(request.POST['filter1'])+'\.*',str(socios[i]['nombre']),re.IGNORECASE)) and
            (re.match(r'.*'+str(request.POST['filter2'])+'\.*',str(socios[i]['apellidos']),re.IGNORECASE)) and
            (re.match(r'.*'+str(request.POST['filter3'])+'\.*',str(socios[i]['dni']),re.IGNORECASE)) and
            (re.match(r'.*'+str(request.POST['filter4'])+'\.*',str(socios[i]['sexo']),re.IGNORECASE)) and
            (re.match(r'.*'+str(request.POST['filter5'])+'\.*',str(socios[i]['seccion']),re.IGNORECASE)) and
            #(re.match(r'.*'+str(request.POST['filter6'])+'\.*',socios[i]['f_nacimiento']),re.IGNORECASE)) and
            (re.match(r'.*'+str(request.POST['filter7'])+'\.*',str(socios[i]['localidad']),re.IGNORECASE)) and
            (re.match(r'.*'+str(request.POST['filter8'])+'\.*',str(socios[i]['provincia']),re.IGNORECASE))
            ):
                selected=True
        
        if selected:
            lista.append(socios[i])
    
    if (
        (
            (str(request.POST['filter0']) != "") and
            (str(request.POST['filter1']) != "") and
            (str(request.POST['filter2']) != "") and
            (str(request.POST['filter3']) != "") and
            (str(request.POST['filter4']) != "") and
            (str(request.POST['filter5']) != "") and
            #(str(request.POST['filter6']) != "") and
            (str(request.POST['filter7']) != "") and
            (str(request.POST['filter8']) != "")) or len(lista) > 0 
        ):  
            datos="ID, Nombre, Apellidos, DNI, Sexo, Seccion, F.Nacimiento, Localidad, Provincia\n"
            for d in range(len(lista)):
                datos += str(lista[d]['id']) + "," + str(lista[d]['nombre']) + "," + str(lista[d]['apellidos']) + "," + str(lista[d]['dni']) + "," + str(lista[d]['sexo']) + "," + str(lista[d]['seccion']) + "," + str(lista[d]['f_nacimiento']) + "," + str(lista[d]['localidad']) + "," + str(lista[d]['provincia']) + "\n"
                
            
            # Insert a file
            media_body = MediaIoBaseUpload(StringIO.StringIO(datos), 'text/csv', resumable=False)
            body = {
              'title': 'Prueba12345',
              'description': 'A test document',
              'mimeType': "text/csv"
            }
            
            file = drive_service.files().insert(body=body, media_body=media_body, convert="true").execute()
            pprint.pprint(file) 
    
    return  HttpResponseRedirect('/')  


def search_familia(request):

    familia= Familia.objects.all()
    
    return render_to_response('socios/search_familia.html', {'familia': familia} ,context_instance=RequestContext(request))

def edit_familia(request, familia_id):
    
    familia = Familia.objects.get(nif=familia_id)
    
    familiares = Familiares.objects.filter(familia_id=familia)
    
    hermanos = Socio.objects.filter(familia_id=familia)
        
    lista = []
        
    for i in range(hermanos.count()):
        lista.extend(D_Personales.objects.filter(socio_id=hermanos[i]))
        
    return render_to_response('socios/f_edit_familiares.html', {'familia': familia, 'familiares': familiares, 'hermanos': lista },context_instance=RequestContext(request))
    
def modify_familia(request):
    
    return None

        