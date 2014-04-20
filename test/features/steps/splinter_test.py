from behave import *
from splinter import Browser

"""
@when(u'visitamos google')
def step1(context):
    with Browser() as browser:
       # Visit URL
      url = "http://www.google.com"
      browser.visit(url)
    pass

@and(u'hacemos la busqueda deseada')
def step2(context):
   browser.fill('q','splinter - python acceptance testing for web applications')
   pass

@then(u'buscamos en boton search y lo presionamos')
def step3(context):
   button = browser.find_by_name('btnG')
   # Interact with elements
   button.click()
   pass

@and(u'terminamos devolviendo true si llegamos a la pagina correcta y false en otro caso.')
def step4(context):
   
   if browser.is_text_present('splinter.cobrateam.info'):
      print "Yes, the official website was found!"
      assert True
   else:
      print "No, it wasn't found... We need to improve our SEO techniques"
      assert False
"""
@then(u'realizamos la prueba')
def visit(context):
   with Browser() as browser:
      # Visit URL
      url = "http://www.google.com"
      browser.visit(url)
      browser.fill('q', 'splinter - python acceptance testing for web applications')
      # Find and click the 'search' button
      button = browser.find_by_name('btnG')
      # Interact with elements
      button.click()
      if browser.is_text_present('splinter.cobrateam.info'):
          print "Yes, the official website was found!"
          assert True
      else:
          print "No, it wasn't found... We need to improve our SEO techniques"
          assert False
