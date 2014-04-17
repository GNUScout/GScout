"""import threading
from wsgiref import simple_server
from selenium import webdriver
from project import model
from socios import web_app

def before_all(context):
    context.server = simple_server.WSGIServer(('', 8000))
    context.server.set_app(web_app.main(environment='test'))
    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()
    context.browser = webdriver.Firefox()

def after_all(context):
    context.server.shutdown()
    context.thread.join()
    context.browser.quit()

def before_feature(context, feature):
    model.init(environment='test')

"""
import logging
 
from selenium import webdriver
 
 
def before_all(context):
   selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
   selenium_logger.setLevel(logging.WARN)
 
   context.driver = webdriver.Firefox()
   context.driver.implicitly_wait(3)
 
 
def after_all(context):
   context.driver.quit()
