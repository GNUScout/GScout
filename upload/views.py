# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from upload.models import Document
from upload.forms import DocumentForm

from socios.models import *

import csv

from datetime import datetime

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #newdoc = Document(docfile = request.FILES['docfile'])
            #newdoc.save()
            paramFile = request.FILES['docfile'].read()
            #portfolio = csv.DictReader(paramFile)
            portfolio = csv.reader(paramFile.splitlines())
            portfolio.next()
           
           # print paramFile
            prueba=[]
            for row in portfolio:
                try:
                    socio = Socio.objects.get(n_asociado = row[0])
                    #Si lo encuentra no hace nada
                except:
                    #De lo contrario comenzamos con el proceso de crearlo
                    # Verificamos que existe un dni con el cual crear un familiar
                    if (row[25] != "") and (row[4] != ""):
                        try:
                            #Si existe el familiar se introduce el socio en la respectiva familia
                            familiar = Familiares.objects.get(nif = row[25])
                            familia = Familia.objects.get(nif = familiar.familia_id.nif)
                        except:
                            #Sino crea una nueva
                            familia = Familia(nombre=row[24],
                                                  apellidos=row[24],
                                                  nif=row[25]
                                                  )
                            familia.save()
                            
                            familiar = Familiares(nombre=row[24],
                                                  apellidos=row[24],
                                                  nif=row[25],
                                                  telefono=row[12],
                                                  movil=row[13],
                                                  familia_id=familia          
                                                  )
                            familiar.save()
                            
                        v_alta = True
                        
                        if row[17] == "0":
                            v_alta = False
                            
                        socio = Socio(n_asociado=row[0],
                                      alta=v_alta,
                                      familia_id=familia)
                        socio.save()
                        
                        datos = D_Personales(nombre = row[1],
                             apellidos = row[2]+" "+row[3],
                             dni = row[5],
                             sexo = "none",
                             f_nacimiento = datetime.strptime(str(row[4]),'%m/%d/%y %H:%M:%S'),
                             direccion = row[8],
                             c_postal = row[9],
                             localidad = row[10],
                             provincia = "S/C de Tenerife",
                             fijo = row[12],
                             movil = row[13],
                             seccion = row[11],
                             socio_id = socio
                             )
                        
                        if row[18] != "":
                            datos.f_baja=datetime.strptime(str(row[18]),'%m/%d/%y %H:%M:%S')
                        
                        if row[16] != "":
                            datos.f_ingreso = datetime.strptime(str(row[16]),'%m/%d/%y %H:%M:%S')
                            
                        datos.save()
                        
                        datos = D_Economicos(titular = row[24],
                             nif_titular = row[25],
                             banco = row[26],
                             sucursal = row[27],
                             d_banco = row[28][0:4],
                             d_sucursal = row[28][4:8],
                             dc = row[28][8:10],
                             n_cuenta = row[28][10:],
                             socio_id = socio
                             )
                        
                        datos.save()
                        
                        datos = D_Medicos(c_seguro= row[7],
                             n_poliza = row[6],
                             t_enfermedad = row[29],
                             t_operado = row[30],
                             t_alergia = row[32],
                             info_adicional = "Deficiencias: \n"+row[31]+"\n\n"+"Medicacion: \n"+row[33]+"\n\n"+"Vacunas: \n"+row[34]+"\n\n"+"Observaciones medicas: \n"+row[35],
                             socio_id = socio
                             )
                        
                        if row[29] != "":
                            datos.enfermedad="si"
                        if row[30] != "":
                            datos.operado="si"
                        if row[32] != "":
                            datos.alergia="si"
                        
                        datos.save()
                            
                        prueba.append(row)
                        
                
                

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('upload.views.list'))
            return render_to_response(
                'upload/list.html',
                {'prueba': prueba},
                context_instance=RequestContext(request)
            )
    
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'upload/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
    