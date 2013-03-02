# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from google.appengine.api import users
from django.shortcuts import render_to_response



def index(request):
    user=users.get_current_user()
 
    
    #return render_to_response('home.html', {
    #                 'user': user,
    #                })
    if (user is None):
        return render_to_response('intro.html')
    else:
        return HttpResponseRedirect('/prueba')