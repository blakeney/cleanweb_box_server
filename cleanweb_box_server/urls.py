from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from cleanweb_box_server import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cleanweb_box_server.views.home', name='home'),
    # url(r'^cleanweb_box_server/', include('cleanweb_box_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Home Page
    url(r'^$', views.home, name='home'),
    
    # Dispatch requests to individual app url files
    url(r'^crowdsource/', include('crowdsource.urls', namespace = 'crowdsource')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
