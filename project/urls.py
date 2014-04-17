from django.conf.urls import patterns, include, url
from socios.views import SignUp,LogIn,LogOut

#Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'project.views.index', name='index'),
    #url(r'^/', include('socios.urls')),
    url(r'^SignUp/$', 'socios.views.SignUp', name='signup'),
    url(r'^LogIn/$', 'socios.views.LogIn', name='login'),
    url(r'LogOut/$','socios.views.LogOut', name='logout'),
    url(r'socios/',include('socios.urls')),
    #url(r'^user/(?P<username>\w+)/',include('socios.urls')),
    #url(r'^profile_view/(?P<username>\w+)/',include('socios.urls')),
    #url(r'^socios/', include('socios.urls')),
    #url(r'^picks/(?P<choice>\w+)/$', 'app.views.picks', name='needed_picks'),
    #url(r'^socios/',include('socios.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
