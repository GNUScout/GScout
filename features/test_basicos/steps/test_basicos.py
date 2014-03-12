# -*- encoding: utf-8 -*-
from behave import *

@then(u'comprobamos la existencia del fichero con la función stat de python')
def step_impl(context):
    import os
    try:
       os.stat("/home/steven/TFG/GScout/urls.py")
       print "Fichero sí existe"
       assert True
    except:
       print "El fichero no existe"
       assert False
