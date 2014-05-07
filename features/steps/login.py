# -*- coding: utf-8 -*
from behave import when,given,then 
from splinter import Browser


@then(u'relleno los campos para el usuario "{user}"')
def escenario1_paso2(context,user):
   password='1234'
   context.splinter.fill('username', user)
   context.splinter.fill('password',password)
   
@step(u'debo estar en la página "{page}"')
def escenario1_paso4(context,page):
   if (context.splinter.url==context.url_base + '/' + page + '/'):
      return True
   else:
      print 'El usuario no puede acceder a su cuenta'
      return False


