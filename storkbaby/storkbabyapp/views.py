# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import render
from django.template import loader
from storkbabyapp.models import user, userRelation, userPreferenceMapping, userChildMapping, review, userExperienceMapping
from django.shortcuts import redirect
from django.db.models import Avg
from urlparse import urlparse 
from .models import review
import re
import urllib

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import NameForm

# This is the landing page for the app!
def index(request, my_id):
    context = {
        'my_id': my_id,
    }
    return render(request,'storkbabyapp/home.html', context)

# This is a user's profile page!
def profile(request, profile_id, my_id):
    # Try to get the user info. Redirect to the landing page if the user doesn't exist.
    person = ""
    try:
        person = user.objects.get(userID=profile_id)
    except:
        return redirect("index")
    # populate data to pass to page
    parent = person.userType
    name = person.name
    address = person.address
    email = person.emailAddress
    # Rating gets its own API call. Currently we take the average of all ratings.
    rating = review.objects.filter(userID__userID__exact=profile_id).aggregate(Avg('rating'))['rating__avg']
    # This will be populated for everyone. NEXT STEP: Should also filter on people the logged in user knows. 
    x = userRelation.objects.filter(userID__userID__exact=profile_id)
    connections = []
    for record in x:
        connections.append([record.relatingUser.name, record.relatingUser.userID])
    # This will be populated but mean something different for sitters/parents
    y = userPreferenceMapping.objects.filter(userID__userID__exact=profile_id)
    preferences = []
    for record in y:
        preferences.append(record.preferenceID.name)
    # Sitter only
    experience = ""
    education = ""
    try:
        exp = userExperienceMapping.objects.get(userID=profile_id)
        experience = exp.education
        education = exp.experience
    except:
        experience = ""
        education = ""
    # Thw below will only populate data for parents. 
    z = userChildMapping.objects.filter(userID__userID__exact=profile_id)
    kids = []
    for record in z:
        kids.append([record.name, record.age])

    # Set up context (determine how to populate as part of template)
    context = {
        'profile_id': profile_id,
        'rating': rating,
        'parent': parent,
        'name' : name,
        'email': email,
        'address': address,
        'connections': connections,
        'preferences': preferences,
        'education': education,
        'experience': experience,
        'kids': kids,
        'my_id': my_id,
    }
    #Return the context rendered with all the data. 
    return render(request, 'storkbabyapp/profile.html', context)

# This is returning a search result!
def results(request, my_id, searched):
    terms = re.split('\+|%20',searched)  
    matched = []
    for term in terms:
        ut = user.objects.filter(name__contains=term)
        for u in ut: 
            if u not in matched:
                matched.append(u)
        pt = userPreferenceMapping.objects.select_related('userID').filter(preferenceID__name__contains=term)
        for p in pt:
            if p.userID not in matched:
                matched.append(p.userID)
    us = []
    for usr in matched:
        quals = []
        upm = userPreferenceMapping.objects.filter(userID__userID__exact=usr.userID)
        for up in upm: 
            quals.append(up.preferenceID.name)
        us.append([usr.name, usr.userID, quals])
    context = {
        'users': us,
        'my_id': my_id
    }
    return render(request, 'storkbabyapp/search.html', context)


#This is the search function!
def search(request, my_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        searchInput = request.POST.get('searchbox')
        print(my_id)
        url = '/storkbaby/' +my_id + '/results/' + urllib.quote(searchInput)
        print(url)
        return HttpResponseRedirect(url)
     
    return HttpResponseRedirect('index', my_id)

#This is the rate function!
def rate(request, my_id, user_id, rating):
    # Try to get the user info. Redirect to the landing page if the user doesn't exist.
    person = ""
    try:
        person = user.objects.get(userID=user_id)
    except:
        return redirect("index")

    reviewer = ""
    try:
        reviewer = user.objects.get(userID=my_id)
    except:
        return redirect("index")

    # Query to save the rating
    ratingSubmission = review(userID=person, reviewer=reviewer, rating=int(rating)+1)
    ratingSubmission.save()
 
    messages.info(request, 'Thank you for your feedback!') 

    return redirect("profile", user_id, my_id)
