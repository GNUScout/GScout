from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index(request):
    context = RequestContext(request) 
    user= request.user # user is the current user
 
    if (user is None): 
        return render_to_response('home2.html',context)
    else:
        #return HttpResponseRedirect('/user/%s/' % user,context)
        return HttpResponseRedirect('/socios/',context)

