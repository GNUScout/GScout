# -*- coding: utf-8 -*-
from socios.forms import UserForm, UserProfileForm
from socios.models import Socio, D_Personales, D_Medicos, D_Economicos, Familia, Familiares, Medicamentos, Autorizaciones

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.sessions.models import Session

import datetime


@login_required
def socios_main_page(request):
   """
      If users are authenticated, direct them to the main page. Otherwise, take
      them to the login page.
     
      **Context**

      ``context``
        An instance of RequestContext(request)


      **Template:**

      :template:`home.html`
   """
   context=RequestContext(request) 
   return render_to_response('home.html',context)

@csrf_protect
def newPersonal(request):
    """View manages the different forms for creating a partner
       
      **Context**

      ``context_instance``
        An instance of RequestContext(request)

      ``errorSocio``
       variable displayed when there is already a partner with the same number of n_asociado

      ``familia``
       variable that contains the members of a given family

      **Template:**

      :template: `socios/f_asociado.html`
      :template: `socios/f_personales.html`
      :template: `socios/f_personales.html`
      :template: `socios/f_familiares.html`
      :template: `socios/f_economicos.html`
      :template: `socios/f_medicos.html`
    """
    
    if request.POST['form_id'] == "f1":
        s_socio = request.session.get('d_socio', {})
               
        s_socio['socio'] = Socio(n_asociado = request.POST['n_asociado']) 
        if (Socio.objects.filter(n_asociado=s_socio['socio'].n_asociado).count() > 0):
            return render_to_response('socios/f_asociado.html', \
                                      {'errorSocio': 'El Número de asociado ya existe.'}, \
                                      context_instance=RequestContext(request))
        else: 
            request.session['d_socio'] = s_socio
            return render_to_response('socios/f_personales.html', \
                                      context_instance=RequestContext(request))
    if request.POST['form_id'] == "f2":
        
        familia = Familiares.objects.all()
        
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
        return render_to_response('socios/f_familiares.html', \
                                  {'familia': familia}, \
                                   context_instance=RequestContext(request))
    if request.POST['form_id'] == "f5":
        
        s_socio = request.session.get('d_socio', {})
        
        
        if request.POST['new_family'] == "si":
            f_nombre = request.POST.getlist('fn[]')
            f_apellidos = request.POST.getlist('fa[]')
            f_nif = request.POST.getlist('fd[]')
            f_rol = request.POST.getlist('fr[]')
            f_tel = request.POST.getlist('ft[]')
            f_movil = request.POST.getlist('fm[]')
            f_email = request.POST.getlist('fe[]')
            
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
            
            s_socio['socio'].familia_id = Familia.objects.get(nif=f_nif[0]) 
            
        else:
            s_socio['socio'].familia_id = Familia.objects.get(nif=request.POST['nif_family'])
            
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
        toma_medicamentos = request.POST['toma_medicamentos']
        
        
        
        datos = D_Medicos(c_seguro= request.POST['c_seguro'],
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
         
        if toma_medicamentos == "si":
            a_nombre = request.POST.getlist('m[]')
            a_dosis = request.POST.getlist('md[]')
            a_pauta = request.POST.getlist('mp[]')
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
     
@login_required
@csrf_protect
def search(request):

    """
     view to seeking a partner for its id    
 
      **Context**

      ``context_instance``
        An instance of RequestContext(request)

      ``errorNoFound``
        if the user is looking for is not there then this variable shows

      **Template:**

      :template:`socios/search.html`
    """

       try:
        socio = Socio.objects.get(n_asociado = request.POST['asociado'])
    except:
        return render_to_response('socios/search.html', \
                                  {'errorNoFound': 'El número de asociado no existe.'}, \
                                  context_instance=RequestContext(request))
    
    return HttpResponseRedirect('/socios/'+socio.n_asociado+'/personales')

def personales_socio(request, n_asociado):
    """ Vista que visualiza los datos personales de un determinado socio"""
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
    
    return render_to_response('socios/datos_personales.html', \
                              {'personales': personales, \
                               'f_nacimiento':personales.f_nacimiento.strftime("%d-%m-%Y"), \
                               'f_ingreso':personales.f_ingreso.strftime("%d-%m-%Y"), \
                               'f_baja': f_baja},RequestContext(request))


def medicos_socio(request, n_asociado):
    """ Vista que visualiza los datos medicos de un determinado socio"""
    try:
        socio = Socio.objects.get(n_asociado=n_asociado)
    except:
        return  HttpResponseRedirect('/socios/search')
    
    medicos = D_Medicos.objects.get(socio_id=socio)
    if medicos.toma_medicamentos == "si":
        medicamentos = Medicamentos.objects.filter(socio_id=socio)
    else:
        medicamentos = None

    
    return render_to_response('socios/datos_medicos.html', {'medicos': medicos, \
                                                            'medicamentos': medicamentos })

def familiares_socio(request, n_asociado):
    """ Vista que visualiza los datos familiares de un determinado socio"""
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
    
        return render_to_response('socios/datos_familiares.html', {'socio': socio, \
                                                                   'familia': familia, \
                                                                   'familiares': familiares, \
                                                                   'hermanos': lista }, \
                                  context_instance=RequestContext(request))
    
    else:
        return  HttpResponseRedirect('/socios/search')


def economicos_socio(request, n_asociado):
    """ Vista que visualiza los datos economicos de un determinado socio"""
    try:
        socio = Socio.objects.get(n_asociado=n_asociado)
    except:
        return  HttpResponseRedirect('/socios/search')
    
    economicos = D_Economicos.objects.get(socio_id=socio)
    
    return render_to_response('socios/datos_economicos.html', {'economicos': economicos })


def edit_personales(request, n_asociado):
    """ Vista que visualiza los posibles datos personales a editar"""
    
    socio = Socio.objects.get(n_asociado=n_asociado)
    personales = D_Personales.objects.get(socio_id=socio)
    
    if personales.f_baja is not None:
        f_baja = personales.f_baja.strftime("%Y-%m-%d")
    else:
        f_baja = "No"
        
    return render_to_response('socios/f_edit_personales.html', {'personales': personales, \
                                                                'f_nacimiento':personales.f_nacimiento.strftime("%Y-%m-%d"), \
                                                                'f_ingreso':personales.f_ingreso.strftime("%Y-%m-%d"), \
                                                                'f_baja': f_baja}, \
                              context_instance=RequestContext(request))

def edit_economicos(request, n_asociado):
    """ Vista que visualiza los posibles datos economicos a editar"""
    
    socio = Socio.objects.get(n_asociado=n_asociado)
    economicos = D_Economicos.objects.get(socio_id=socio)
       
    return render_to_response('socios/f_edit_economicos.html', {'economicos': economicos} , \
                              context_instance=RequestContext(request))

def edit_medicos(request, n_asociado):
    """ Vista que visualiza los posibles datos medicos a editar"""
    
    socio = Socio.objects.get(n_asociado=n_asociado)
    medicos = D_Medicos.objects.get(socio_id=socio)
    medicamentos = Medicamentos.objects.filter(socio_id=socio)
    n_medicamentos = medicamentos.count()
    
   
    
    return render_to_response('socios/f_edit_medicos.html', {'medicos': medicos, \
                                                             'medicamentos': medicamentos, \
                                                             "n_medicamentos" : n_medicamentos } , \
                              context_instance=RequestContext(request))


def modify_personales(request):
    """ Vista que gestiona la modificación de los datos personales"""
    
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
    """ Vista que gestiona la modificación de los datos economicos"""
    
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
    """ Vista que gestiona la modificación de los datos medicos"""
    
    total_medicamentos = request.POST['total_medicamentos']
    
    socio = D_Medicos.objects.get(socio_id= request.POST['socio'])
    socio.c_seguro = request.POST['c_seguro']
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
        a_nombre = request.POST.getlist('m[]')
        a_dosis = request.POST.getlist('md[]')
        a_pauta = request.POST.getlist('mp[]')
        for i in range(len(a_nombre)):
            medicamento = Medicamentos(nombre=a_nombre[i],
                                        dosis=a_dosis[i],
                                        pauta=a_pauta[i],
                                        socio_id=socio.socio_id
                                        )
            medicamento.save()
    
    
   
    return  HttpResponseRedirect('/socios/'+socio.socio_id.n_asociado+'/medicos')

@login_required
def listado(request):
    """ Vista que muestra un listado de los datos personales de los socios"""
    socios = D_Personales.objects.all()
    
    for s in socios:
        s.f_nacimiento = s.f_nacimiento.strftime('%b %d, %Y')
     
    return render_to_response('socios/list.html', {'socios': socios} , \
                              context_instance=RequestContext(request))

@login_required
def listado_del(request):
    """ Vista que muestra todos los socios que se pueden eliminar"""
    socios = D_Personales.objects.all()
    
    for s in socios:
        s.f_nacimiento = s.f_nacimiento.strftime('%b %d, %Y')
     
    return render_to_response('socios/list_del.html', {'socios': socios} , \
                              context_instance=RequestContext(request))
@login_required
@csrf_protect
def listado_economicos(request):
    """ Vista que muestra los datos economicos de los socios en forma de listado"""
    socios = D_Personales.objects.all()
    
    economicos = D_Economicos.objects.all()
    
    lista = zip(socios, economicos)
     
    return render_to_response('socios/listado_economicos.html', {'lista': lista} , \
                              context_instance=RequestContext(request))

def del_socios(request):
    """ Vista que gestiona la eliminacion permanente de socios"""
    sel_socios = request.POST.getlist('sel_borrar[]')

    for i in range(len(sel_socios)):
        lista_medicamentos = Medicamentos.objects.filter(socio_id=sel_socios[i])
        for j in lista_medicamentos:
            j.delete()
        aux = D_Medicos.objects.get(socio_id=sel_socios[i])
        aux.delete()
        aux = D_Economicos.objects.get(socio_id=sel_socios[i])
        aux.delete()
        aux = D_Personales.objects.get(socio_id=sel_socios[i])
        aux.delete()
        aux = Socio.objects.get(n_asociado=sel_socios[i])
        aux.delete()
    
    socios = D_Personales.objects.all()
    
    return render_to_response('socios/list_del.html', {'socios': socios} , \
                              context_instance=RequestContext(request))
            
@login_required
def search_familia(request):
    """Vista de los listados de familias"""

    familia = Familia.objects.all()
    
    return render_to_response('socios/search_familia.html', {'familia': familia} , \
                              context_instance=RequestContext(request))

def edit_familia(request, familia_id):
    """Vista que muestra las familias que se pueden editar"""
    familia = Familia.objects.get(nif=familia_id)
    
    familiares = []
    
    familiares.extend(Familiares.objects.filter(nif=familia_id))
    
    todos = Familiares.objects.filter(familia_id=familia)
    for i in todos:
        if i.nif != familia_id:
            familiares.extend([i]) 
    
    
    hermanos = Socio.objects.filter(familia_id=familia)
        
    lista = []
        
    for i in range(hermanos.count()):
        lista.extend(D_Personales.objects.filter(socio_id=hermanos[i]))
        
    
        
    return render_to_response('socios/f_edit_familiares.html', {'familia': familia, \
                                                                'familiares': familiares, \
                                                                'hermanos': lista }, \
                              context_instance=RequestContext(request))
    
    
def modify_familia(request):
    """Vista que modifica la familia con los datos que se le han pasado"""    
    
    familia_old = Familia.objects.get(nif=request.POST['oldfamily'])
    
    hijos = Socio.objects.filter(familia_id = familia_old)
    
    familiares_old = Familiares.objects.filter(familia_id=familia_old)
    for f in familiares_old:
        f.delete()
    
    familia_old.delete()
    
    a_nombre = request.POST.getlist('fn[]')
    a_apellidos = request.POST.getlist('fa[]')
    a_nif = request.POST.getlist('fd[]')
    a_rol = request.POST.getlist('fr[]')
    a_telefono = request.POST.getlist('ft[]')
    a_movil = request.POST.getlist('fm[]')
    a_email = request.POST.getlist('fe[]')
    
    familia_new = Familia(nif = a_nif[0],
                          nombre = a_nombre[0],
                          apellidos = a_apellidos[0])
    
    familia_new.save()
    
    for i in range(len(a_nombre)):
        familiar = Familiares(nombre = a_nombre[i],
                              apellidos = a_apellidos[i],
                              nif = a_nif[i],
                              rol = a_rol[i],
                              telefono = a_telefono[i],
                              movil = a_movil[i],
                              email = a_email[i],
                              familia_id = familia_new)
        familiar.save()
      
    for i in hijos:
        i.familia_id = familia_new
        i.save()
       
    
    
    return  HttpResponseRedirect('/socios/'+familia_new.nif+'/edit_familiares')

def change_familia(request, n_asociado):
    """Vista para la visualizacion de las posibles familiares a editar"""
    
    familia = Familiares.objects.all()
    
    return render_to_response('socios/f_change_familia.html', {'socio': n_asociado, \
                                                               'familia': familia}, \
                              context_instance=RequestContext(request))
    
def post_change_familia(request):
    """Vista de post para los cambios de familia"""     
    socio = Socio.objects.get(n_asociado=request.POST["n_asociado"])
        
    if request.POST['new_family'] == "si":
        f_nombre = request.POST.getlist('fn[]')
        f_apellidos = request.POST.getlist('fa[]')
        f_nif = request.POST.getlist('fd[]')
        f_rol = request.POST.getlist('fr[]')
        f_tel = request.POST.getlist('ft[]')
        f_movil = request.POST.getlist('fm[]')
        f_email = request.POST.getlist('fe[]')
        
        new = Familia(nombre = f_nombre[0],
                      apellidos = f_apellidos[0],
                      nif = str(f_nif[0]),
                      )
        new.save()
        
        for i in range(len(f_nombre)):
            familiar = Familiares(nombre = f_nombre[i],
                                       apellidos = f_apellidos[i],
                                       nif = f_nif[i],
                                       rol = f_rol[i],
                                       telefono = f_tel[i],
                                       movil = f_movil[i],
                                       email = f_email[i],
                                       familia_id = Familia.objects.get(nif=str(f_nif[0]))
                                       )
            familiar.save()
        
        socio.familia_id = Familia.objects.get(nif=f_nif[0]) 
        
    else:
        socio.familia_id = Familia.objects.get(nif=request.POST['nif_family'])
        
    socio.save()
        
    return HttpResponseRedirect('socios/'+request.POST["n_asociado"]+"/familiares")   

def cambio_unidad(request):  
    """ Vista para el cambio de unidad en los socios"""
    socios = D_Personales.objects.all()
    
    date = datetime.datetime.now()
    date = int(date.strftime('%Y'))
    
    for s in socios:
        if (date - int(s.f_nacimiento.strftime('%Y')))  < 11 :
            s.seccion = "Manada"
        if ((date - int(s.f_nacimiento.strftime('%Y'))  >= 11) and \
            (date - int(s.f_nacimiento.strftime('%Y'))  < 14)):
            s.seccion = "Tropa"
        if ((date - int(s.f_nacimiento.strftime('%Y'))  >= 14) and \
            (date - int(s.f_nacimiento.strftime('%Y'))  < 17)):
            s.seccion = "Esculta"
        if ((date - int(s.f_nacimiento.strftime('%Y'))  >= 17) and \
            (date - int(s.f_nacimiento.strftime('%Y'))  < 20)):
            s.seccion = "Rover" 
        if (date - int(s.f_nacimiento.strftime('%Y')))  >= 20 :
            s.seccion = "Scouter" 
        
        s.save()
            
    return HttpResponseRedirect('/')   
