from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<profile_id>[0-9]+)/profile/$', views.results, name='results'),
    url(r'^(?P<profile_id>[0-9]+)/search/$', views.search, name='search'),
]
