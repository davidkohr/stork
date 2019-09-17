# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import users, preferences, userPreferenceMapping, reviews, userRelations

admin.site.register(users)
admin.site.register(preferences)
admin.site.register(userPreferenceMapping)
admin.site.register(reviews)
admin.site.register(userRelations)

