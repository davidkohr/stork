# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import user, preference, userPreferenceMapping, review, userRelation

admin.site.register(user)
admin.site.register(preference)
admin.site.register(userPreferenceMapping)
admin.site.register(review)
admin.site.register(userRelation)

