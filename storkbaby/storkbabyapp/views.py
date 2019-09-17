# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

# This is the landing page for the app!
def index(request):
    return render(request,'storkbabyapp/home.html')

# This is a user's profile page!
def results(request, profile_id):
    # This is where we would do some DB queries to get profile info

    # Declaring some very basic variables to test with. 
    parent = True
    firstname = "Jane"
    lastname = "Doe"
    email = "jane.doe@indexexchange.com"
    phone = "(416) 555-5555"
    # This will be populated for everyone
    connections = [["Friend", "Best", 1], ["Sister", "Oldest", 2], ["Friend", "Other", 3], ["Co", "Worker", 4]]
    # This will be populated but mean something different for sitters/parents
    preferences = ["vegetarian","ADHD support"]
    # Sitter only
    education = ""
    experience = ""
    # Parent only
    kids = [["Bobby", "Doe", 11],["Alice", "Doe", 8]]

    # Set up context (determine how to populate as part of template)
    context = {
        'profile_id': profile_id,
        'parent': parent,
        'firstname' : firstname,
        'lastname' : lastname,
        'email': email,
        'phone': phone,
        'connections': connections,
        'preferences': preferences,
        'education': education,
        'experience': experience,
        'kids': kids,
    }

    return render(request, 'storkbabyapp/profile.html', context)