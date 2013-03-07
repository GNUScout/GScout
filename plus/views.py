import os
import logging
import settings
import httplib2

from apiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from plus.models import CredentialsModel
from django.contrib.auth.models import User



from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage
from oauth2client.client import OAuth2WebServerFlow

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json')

FLOW = OAuth2WebServerFlow (
    client_id ='480482329789-dj8a6lggtm9cpml3oib7imbvs3b9fv4q.apps.googleusercontent.com',
    client_secret = 'C5umC7xa_ML704wnmdT79Bh0',
    token_uri='https://accounts.google.com/o/oauth2/token',
    scope='https://www.googleapis.com/auth/plus.me',
    redirect_uri= 'http://localhost:8000/oauth2callback', #'http://ctstprueba.appspot.com/oauth2callback',
    access_type='offline',
    approval_prompt='force')

@login_required
def index(request):
    usuario = request.user
    storage = User.objects.get(username = usuario.username) #Storage(CredentialsModel, 'id', request.user, 'credential')
    
    credential = storage.credential #storage.get()
    if credential is None or credential.invalid == True:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                   request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        service = build('plus', 'v1', http=http)
        user = request.user
        people_resource = service.people()    
        people_document = people_resource.get(userId='me').execute()
        people_id = "ID: " + people_document['id']
        people_name = "Display name: " + people_document['displayName']
        people_image = people_document['image']['url']
    
        return render_to_response('home.html', {
                    'people_id': people_id, 'people_name': people_name, 'people_image': people_image, 'user': user,
                    })


@login_required
def auth_return(request):
    if not xsrfutil.validate_token(settings.SECRET_KEY, request.REQUEST['state'],
                                 request.user):
        return  HttpResponseBadRequest()
    credential = FLOW.step2_exchange(request.REQUEST)
    http = httplib2.Http()
    http = credential.authorize(http)
    service = build('plus', 'v1', http=http)
    usuario = request.user
    usuario.credential = credential #storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    usuario.save()#storage.put(credential)
    return HttpResponseRedirect("/")
