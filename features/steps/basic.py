# -*- encoding: utf-8 -*-
import os
from behave import *

ruta_absoluta="/home/steven/TFG/GScout/"

@then(u'comprobamos la existencia del fichero "{fich}" con la función stat de python')
def step_impl(context,fich):
    try:
       os.stat(ruta_absoluta+fich)
       print "Fichero sí existe"
       assert True
    except:
       print "El fichero no existe"
       assert False
