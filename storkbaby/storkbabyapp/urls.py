from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<profile_id>[0-9]+)/profile/$', views.profile, name='profile'),
    url(r'^results/(?P<searched>[A-z0-9]+)$', views.results, name='search'),
    url(r'^search$', views.search, name='search'),
]
