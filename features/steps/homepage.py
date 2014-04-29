# -*- coding: utf-8 -*-

from behave import when,given,then,And,but #Step and como And si no reconoce and como función de python
from splinter import Browser

#paso definido en el atecedente por lo que se repetirá antes de cada escenario
@when(u'estoy en la página inicial')
def antecedente_paso1(context):
   url = "http://localhost:8000"
   context.splinter.visit(url)  
   return True

@then(u'compruebo que existe un título y que además es "{titulo}"')
def escenario1_paso3(context,titulo):
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


