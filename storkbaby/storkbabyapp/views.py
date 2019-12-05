# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from storkbabyapp.models import pup
from django.template.response import TemplateResponse


# This is the landing page for the app!
def home(request):
    ix_pups = []
    query_set = pup.objects.all()
    for single_pup in query_set:
        ix_pups.append([single_pup.name, single_pup.picture.url, single_pup.description, single_pup.owner])
    return TemplateResponse(request, 'storkbabyapp/home.html', {'ix_pups': ix_pups})
