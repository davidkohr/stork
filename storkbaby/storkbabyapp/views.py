# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from storkbabyapp.models import pup
from django.template.response import TemplateResponse

from .forms import NewDogForm


# This is the landing page for the app!
def home(request):
    ix_pups = []
    if request.method == 'POST':
        form = NewDogForm(request.POST, request.FILES)
        if form.is_valid():
            if not pup.objects.filter(name=form.cleaned_data['name']):
                pup.objects.create(name=form.cleaned_data['name'], description=form.cleaned_data['description'], owner=form.cleaned_data['owner'], picture=request.FILES['picture'])
        else:
            return TemplateResponse(request, 'storkbabyapp/home.html', {'ix_pups': ix_pups, 'form': form})
    query_set = pup.objects.all()
    for single_pup in query_set:
        ix_pups.append([single_pup.name, single_pup.picture.url, single_pup.description, single_pup.owner])
    form = NewDogForm(initial={'name': '', 'description': '', 'owner': ''})
    return TemplateResponse(request, 'storkbabyapp/home.html', {'ix_pups': ix_pups, 'form': form})
