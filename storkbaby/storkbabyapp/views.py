# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# This is the landing page for the app!
def index(request):
    return HttpResponse("Hello, world. You're at the storkbaby index.")

# This is a user's profile page!
def results(request, profile_id):
    response = "You're looking at the profile for user %s."
    return HttpResponse(response % profile_id)