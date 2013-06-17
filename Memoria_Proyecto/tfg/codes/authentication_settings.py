# -*- coding: utf-8 -*-
.  

INSTALLED_APPS = (
    .            
    'plus',
    'gaeauth',
    'djangoappengine',
    .    
)

.  

AUTHENTICATION_BACKENDS = (
      'gaeauth.backends.GoogleAccountBackend',
)
ALLOWED_DOMAINS = ('gruposcoutaguere70.org',)
