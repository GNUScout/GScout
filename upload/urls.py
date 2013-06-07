# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from upload.views import *

urlpatterns = patterns('upload.views',
    url(r'^upload_file/$', upload_file),
)