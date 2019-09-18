# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from storkbabyapp.models import user, userRelation, userPreferenceMapping, userChildMapping, review, userExperienceMapping
from django.shortcuts import redirect

import re
import urllib

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# This is the landing page for the app!
def home(request):
    return render(request,'storkbabyapp/home.html')
