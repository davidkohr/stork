# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
    userID = models.IntegerField(default=0)
    userType = models.IntegerField(default=0)
    emailAddress = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)


class preferences(models.Model):
    preferenceID = models.IntegerField(default=0)
    name = models.CharField(max_length=255)


class userPreferenceMapping(models.Model):
    userID = models.ForeignKey(users, related_name="%(class)s_userID")
    preferenceID = models.ForeignKey(preferences, related_name="%(class)s_preferenceID")


class reviews(models.Model):
    user = models.ForeignKey(users, null=True, related_name="%(class)s_user")
    reviewer = models.ForeignKey(users, null=True, related_name="%(class)s_reviewer")
    preferenceID = models.ForeignKey(
        preferences, null=True, related_name="%(class)s_preferenceID")
    rating = models.IntegerField(default=0)


class userRelations(models.Model):
    userID = models.ForeignKey(users, related_name="%(class)s_userID")
    relatingUser = models.ForeignKey(users, related_name="%(class)s_relatingUser")
