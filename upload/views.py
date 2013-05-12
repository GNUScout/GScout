# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from upload.models import Document
from upload.forms import DocumentForm

import csv

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #newdoc = Document(docfile = request.FILES['docfile'])
            #newdoc.save()
            paramFile = request.FILES['docfile'].read()
            #portfolio = csv.DictReader(paramFile)
            portfolio = csv.reader(paramFile.splitlines())
           
           # print paramFile
            prueba=[]
            for row in portfolio:
                prueba.append(row)

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('upload.views.list'))
            return render_to_response(
                'upload/list.html',
                {'prueba': prueba},
                context_instance=RequestContext(request)
            )
    
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'upload/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
    