# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import users, preferences, userPreferenceMapping, reviews, userRelations, userChildMapping, userExperienceMapping

admin.site.register(user)
admin.site.register(preference)
admin.site.register(userPreferenceMapping)
admin.site.register(reviews)
admin.site.register(userRelations)
admin.site.register(userChildMapping)
admin.site.register(userExperienceMapping)
