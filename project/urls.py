#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns,include,url

urlpatterns = patterns('project.views',
    (r'^$', 'main_page'), 
    (r'^register/$','register'),
    (r'^login/$', 'login'),
    (r'^logout/$', 'logout'),
   
    (r'^socios/',include('socios.urls')),
    #url(r'^user/(?P<username>\w+)/',include('socios.urls')),
    #url(r'^profile_view/(?P<username>\w+)/',include('socios.urls')),
    #url(r'^picks/(?P<choice>\w+)/$', 'app.views.picks', name='needed_picks'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
