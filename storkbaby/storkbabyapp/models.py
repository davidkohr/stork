# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    userID = models.IntegerField(default=0)
    userType = models.IntegerField(default=0)
    emailAddress = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)


class preference(models.Model):
    preferenceID = models.IntegerField(default=0)
    name = models.CharField(max_length=255)


class userPreferenceMapping(models.Model):
    userID = models.ForeignKey(user, related_name="%(class)s_userID")
    preferenceID = models.ForeignKey(preference, related_name="%(class)s_preferenceID")


class review(models.Model):
    users = models.ForeignKey(user, null=True, related_name="%(class)s_users")
    reviewer = models.ForeignKey(user, null=True, related_name="%(class)s_reviewer")
    preferenceID = models.ForeignKey(
        preference, null=True, related_name="%(class)s_preferenceID")
    rating = models.IntegerField(default=0)


class userRelation(models.Model):
    userID = models.ForeignKey(user, related_name="%(class)s_userID")
    relatingUser = models.ForeignKey(user, related_name="%(class)s_relatingUser")
