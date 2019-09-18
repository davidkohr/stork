from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<my_id>[0-9]+)/$', views.index, name='index'),
    url(r'^(?P<my_id>[0-9]+)/(?P<profile_id>[0-9]+)/profile/$', views.profile, name='profile'),
    url(r'^(?P<my_id>[0-9]+)/results/(?P<searched>[A-z0-9\+]+)$', views.results, name='results'),
    url(r'^(?P<my_id>[0-9]+)/search$', views.search, name='search'),
]
