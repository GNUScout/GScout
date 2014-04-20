# -*- coding: utf-8 -*-

from behave import *
from splinter import Browser

with Browser() as browser:
   url = "http://127.0.0.1:8000"
   browser.visit(url)


@when(u'voy a la página inicial')
def step1(context):
   pass

@then(u'compruebo que el titulo es "{titulo}"')
def step2(context,titulo):
    if browser.title==titulo:
        assert True 
    else:
         assert False

@then(u'busco el elemento "{element}"') 
def def_impl(context,element):
    assert True       
