# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('upload.views',
    url(r'^list/$', 'list', name='list'),
)