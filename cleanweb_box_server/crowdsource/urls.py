from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'views.home', name='crowdsource_home'),
    url(r'^upload', 'views.upload', name='crowdsource_upload'),
    url(r'^thanks$', 'views.thanks', name='crowdsource_thanks'),
)
