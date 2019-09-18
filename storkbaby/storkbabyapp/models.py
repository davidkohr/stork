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
    def __str__(self):
        return '%s: %s' % (self.userID, self.name)

class preference(models.Model):
    preferenceID = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    def __str__(self):
        return '%s: %s' % (self.preferenceID, self.name)

class userChildMapping(models.Model):
    userID = models.ForeignKey(user, related_name="%(class)s_userID")
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    def __str__(self):
        return '%s: %s, %s' % (self.userID, self.name, self.age)

class userExperienceMapping(models.Model):
    userID = models.ForeignKey(user, related_name="%(class)s_userID")
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    def __str__(self):
        return '%s: %s, %s' % (self.userID, self.education, self.experience)

class userPreferenceMapping(models.Model):
    userID = models.ForeignKey(user, related_name="%(class)s_userID")
    preferenceID = models.ForeignKey(preference, related_name="%(class)s_preferenceID")
    def __str__(self):
        return '%s: %s' % (self.userID, self.preferenceID)

class review(models.Model):
    userID = models.ForeignKey(user, null=True, related_name="%(class)s_userID")
    reviewer = models.ForeignKey(user, null=True, related_name="%(class)s_reviewer")
    preferenceID = models.ForeignKey(preference, null=True, related_name="%(class)s_preferenceID")
    rating = models.IntegerField(default=0)
    def __str__(self):
        return '%s: %s - %s' % (self.userID, self.reviewer, self.rating)

class userRelation(models.Model):
    userID = models.ForeignKey(user, related_name="%(class)s_userID")
    relatingUser = models.ForeignKey(user, related_name="%(class)s_relatingUser")
    def __str__(self):
        return '%s --> %s' % (self.userID, self.relatingUser)
