# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the storkbaby index.")

def profile(request):
    return HttpResponse("Hello, world. You're at the storkbaby profile page.")