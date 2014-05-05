# -*- coding: utf-8 -*-
import time
from behave import when,given,then,And,but #Step and como And si no reconoce and como función de python
from splinter import Browser

#paso definido en el atecedente por lo que se repetirá antes de cada escenario
@when(u'estoy en la página inicial')
def antecedente_paso1(context):
   url = "http://localhost:8000"
   context.splinter.visit(url)  
   return True

@then(u'compruebo que existe un título y que además es "{titulo}"')
def escenario1_paso2(context,titulo):
    if ((context.splinter.is_element_not_present_by_tag('title')==False) & (context.splinter.title==titulo) ):
        assert True
    else:
        assert False
     
@then(u'busco el elemento "{element1}" y "{element2}"') 
def escenario2_paso2(context,element1,element2):
   if (context.splinter.is_element_present_by_tag(element1)) & (context.splinter.is_element_present_by_tag(element2)):
      assert True
   else:
      assert False

#and lo coge como then
@then(u'compruebo que existe un elemento "{element}"')
def escenario2_paso3(context,element):
   if (context.splinter.is_element_present_by_tag(element)):
      assert True
   else:
      assert False    


@then(u'un mensaje de bienvenida')
def escenario2_paso4(context):
   if (context.splinter.is_text_present('Bienvenido a')): 
      assert True
   else:
      assert False

@then(u'busco el botón "{btn}"')
def escenario3_paso2(context,btn):
   #if (context.splinter.is_element_present_by_xpath('btn btn-large btn-primary')):
   context.boton=context.splinter.find_link_by_text(btn)
   if (context.boton.is_empty()):
      assert False
   else:
      #context.boton.click()
      #time.sleep(6)
      assert True

@then(u'lo presiono')
def escenario3_paso3(context):
   context.boton.click()
   if (context.splinter.is_text_present('Register with GSCout')):
      assert True
   else:
      assert False

@then(u'relleno los campos para el usuario "{user}"')
def escenario3_paso4(context,user):
   #username=user
   password='1234'
   context.splinter.fill('username', user)
   context.splinter.fill('email', user + '@gmail.com')
   context.splinter.fill('password', password)
   context.splinter.fill('website', user + '.com')
   #time.sleep(6)
   return True

@then(u'me registro')
def escenario3_paso5(context):
    context.boton=context.splinter.find_by_name('submit')
    if (context.boton.is_empty()):
      assert False
    else:
      context.boton.click()
      time.sleep(6)
      assert True





