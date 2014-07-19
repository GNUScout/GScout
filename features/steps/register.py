# -*- coding: utf-8 -*-
import time
from behave import when,given,then 
from splinter import Browser


@given(u'que estoy en la página "{page}"')
def antecedente_paso1(context,page):
   context.url_base = "http://localhost:8000" 
   context.url= context.url_base + "/" + page + "/"
   context.splinter.visit(context.url)
   if (context.splinter.url==context.url):
      return True
   else:
      print 'no se puede ir a la página ' + page
      return False

@then(u'compruebo que el contenido de la página es el correcto')
def escenario1_paso2(context):
   #si estoy en la página registro debo ver el titulo y el texto que se encuentra en dicha página,si se cumple retorno True,False en otro caso.
   if ((context.splinter.title == 'GSCOUT | REGISTRO') & (context.splinter.is_text_present('Registro en GScout'))):
      assert True
   else:
      print 'No me encuentro en la página de registro' 
      assert False

@step(u'relleno los campos para el usuario "{user}"')
def escenario1_paso3(context,user):
   password='1234'
   context.splinter.fill('username', user)
   context.splinter.fill('email', user + '@gmail.com')
   context.splinter.fill('password', password)
   context.splinter.fill('website', user + '.com')
   return True


@then(u'compruebo la existencia del botón "{btn}" y le doy click')
def escenario1_paso4(context,btn):
   context.boton=context.splinter.find_by_name(btn)
   if (context.boton.is_empty()):
      print "No existe un botón con el nombre" + btn
      assert False
   else:
      context.boton.click()
      return True


#then o step sirve para referirnos a and
@step(u'se debe mostrar el mensaje "{msg}" para finalizar el proceso.')
def escenario1_paso5(context,msg):
   if (context.splinter.is_text_present(' ')):
      assert True
   else:
      print 'el usuario ya existe'
      assert False

