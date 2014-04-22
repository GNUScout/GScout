# -*- coding: utf-8 -*-

from behave import *
from splinter import Browser

b=Browser()

@when(u'voy a la página inicial')
def escenario1_paso1(context): 
   url = "http://localhost:8000"
   b.visit(url)
   return True


@then(u'compruebo que existe un titulo y que ademas es "{titulo}"')
def escenario1_paso3(context,titulo):
    if ((b.is_element_not_present_by_tag('title')==False) & (b.title==titulo) ):
        assert True
    else:
        assert False
     
@then(u'busco el elemento "{element1}" y "{element2}"') 
def escenario2_paso2(context,element1,element2):
   if (b.is_element_present_by_tag(element1)) & (b.is_element_present_by_tag(element2)):
      assert True
   else:
     assert False

#b.quit()

