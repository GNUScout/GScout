"""environment --environmental setup for Django+Behave+Mechanize
 
This should go in features/environment.py
(http://packages.python.org/behave/tutorial.html#environmental-controls)
 
Requirements:
http://pypi.python.org/pypi/behave/
http://pypi.python.org/pypi/mechanize/
http://pypi.python.org/pypi/wsgi_intercept
http://pypi.python.org/pypi/BeautifulSoup/
 
Acknowledgements:
For the basic solution: https://github.com/nathforge/django-mechanize/
 
"""
import os
# This is necessary for all installed apps to be recognized, for some reason.
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
 
 
def before_all(context):
   # Even though DJANGO_SETTINGS_MODULE is set, this may still be
   # necessary. Or it may be simple CYA insurance.
   from django.core.management import setup_environ
   from myproject import settings
   setup_environ(settings)
 
   from django.test import utils
   utils.setup_test_environment()
 
   ## If you use South for migrations, uncomment this to monkeypatch
   ## syncdb to get migrations to run.
   # from south.management.commands import patch_for_test_db_setup
   # patch_for_test_db_setup()
 
   ### Set up the WSGI intercept "port".
   import wsgi_intercept
   from django.core.handlers.wsgi import WSGIHandler
   host = context.host = 'localhost'
   port = context.port = getattr(settings, 'TESTING_MECHANIZE_INTERCEPT_PORT', 17681)
   # NOTE: Nothing is actually listening on this port. wsgi_intercept
   # monkeypatches the networking internals to use a fake socket when
   # connecting to this port.
   wsgi_intercept.add_wsgi_intercept(host, port, WSGIHandler)
 
   import urlparse
   def browser_url(url):
      """Create a URL for the virtual WSGI server.
      e.g context.browser_url('/'), context.browser_url(reverse('my_view'))
      """
      return urlparse.urljoin('http://%s:%d/' % (host, port), url)
 
   context.browser_url = browser_url
 
### BeautifulSoup is handy to have nearby. (Substitute lxml or html5lib as you see fit)
from BeautifulSoup import BeautifulSoup
def parse_soup():
   """Use BeautifulSoup to parse the current response and return the DOM tree.
   """
   r = context.browser.response()
   html = r.read()
   r.seek(0)
   return BeautifulSoup(html)
 
context.parse_soup = parse_soup
 
 
def before_scenario(context, scenario):
   # Set up the scenario test environment
 
   # We must set up and tear down the entire database between
   # scenarios. We can't just use db transactions, as Django's
   # TestClient does, if we're doing full-stack tests with Mechanize,
   # because Django closes the db connection after finishing the HTTP
   # response.
   from django.db import connection
   connection.creation.create_test_db(verbosity=1, autoclobber=True)
 
   ### Set up the Mechanize browser.
   from wsgi_intercept import mechanize_intercept
   # MAGIC: All requests made by this monkeypatched browser to the magic
   # host and port will be intercepted by wsgi_intercept via a
   # fake socket and routed to Django's WSGI interface.
   browser = context.browser = mechanize_intercept.Browser()
   browser.set_handle_robots(False)
 
 
def after_scenario(context, scenario):
   # Tear down the scenario test environment.
   from django.db import connection
   connection.creation.destroy_test_db(verbosity=1, autoclobber=True)
   # Bob's your uncle.
 
 
def after_all(context):
   from django.test import utils
   utils.teardown_test_environment()


