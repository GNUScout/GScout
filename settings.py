""" Archivo setting.py"""

# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
import os.path

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
      'NAME': '',                      # Or path to database file if using sqlite3.
      'USER': '',                      # Not used with sqlite3.
      'PASSWORD': '',                  # Not used with sqlite3.
      'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
      'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
   }
}


SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

SITE_ID = 1

DEBUG = True


INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'djangotoolbox',
    'django.contrib.staticfiles',
    'socios',
    
       
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static', 
)

AUTHENTICATION_BACKENDS = (
  
)
   
# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = os.path.join(PROJECT_ROOT, 'templates')  

ROOT_URLCONF = 'urls'

STATIC_URL = '/static/'

STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

