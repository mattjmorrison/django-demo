from django.conf.urls import patterns, include, url
from sample import views


urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='home'),
    url(r'^pick/$', views.Picker.as_view(), name='picker'),
)
