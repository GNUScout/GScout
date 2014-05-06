# -*- coding: utf-8 -*-
import time
from behave import when,given,then,And,but #Step and como And si no reconoce and como función de python
from splinter import Browser

#paso definido en el atecedente por lo que se repetirá antes de cada escenario
@when(u'estoy en la página inicial')
def antecedente_paso1(context):
   context.url_base = "http://localhost:8000"
   context.splinter.visit(context.url_base)  
   return True

@then(u'compruebo que existe un título y que además es "{titulo}"')
def escenario1_paso2(context,titulo):
    if (context.splinter.is_element_not_present_by_tag('title')==False):
       if (context.splinter.title==titulo):    
          assert True
       else:
          print 'El titulo no se corresponde con el que debiera tener la página principal.'
          assert False
    else:
        print 'La página principal no tiene un titulo llamado ' + titulo
        assert False
     
@then(u'busco el elemento "{element1}" y "{element2}"') 
def escenario2_paso2(context,element1,element2):
   if (context.splinter.is_element_present_by_tag(element1)) & (context.splinter.is_element_present_by_tag(element2)):
      assert True
   else:
      print 'la página web no tiene un elemento ' + element1 + 'ni ' + element2
      assert False

#then o step pueden hacer referencia a and
@step(u'compruebo que existe un elemento "{element}"')
def escenario2_paso3(context,element):
   if (context.splinter.is_element_present_by_tag(element)):
      assert True
   else:
      print 'la página web no tiene un elemento ' + element
      assert False    

@step(u'un mensaje de bienvenida')
def escenario2_paso4(context):
   if (context.splinter.is_text_present('Bienvenido a')): 
      assert True
   else:
      print 'No hay un mensaje de bienvenida que concuerde con el dado'
      assert False

@then(u'busco el botón "{btn}"')
def escenario3_paso2(context,btn):
   #if (context.splinter.is_element_present_by_xpath('btn btn-large btn-primary')):
   context.boton=context.splinter.find_link_by_text(btn)
   if (context.boton.is_empty()):
      print 'No existe el botón ' + btn
      assert False
   else:
      #context.boton.click()
      #time.sleep(6)
      assert True

@step(u'compruebo que estoy en la página "{page}"')
def escenario3_paso3(context,page):
   context.boton.click()
   if (context.splinter.url == context.url_base+page):
      assert True
   else:
      print 'No estoy en la página ' + context.url_base+page
      assert False


