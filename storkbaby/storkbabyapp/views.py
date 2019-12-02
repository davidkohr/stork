# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# This is the landing page for the app!
def home(request):
    return render(request, 'storkbabyapp/home.html')
