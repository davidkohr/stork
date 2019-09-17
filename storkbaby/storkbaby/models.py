from django.db import models


class users(models.Model):
    userID = models.IntegerField(default=0)
    userType = models.IntegerField(default=0)
    emailAddress = models.CharField(max_length=None)
    name = models.CharField(max_length=None)
    address = models.CharField(max_length=None)


class preferences(models.Model):
    preferenceID = models.IntegerField(default=0)
    name = models.CharField(max_length=None)


class userPreferenceMapping(models.Model):
    userID = models.ForeignKey(users, related_name='userID')
    preferenceID = models.ForeignKey(preferences, related_name='preferenceID')


class reviews(models.Model):
    user = models.ForeignKey(users, null=True, related_name='user')
    reviewer = models.ForeignKey(users, null=True, related_name='reviewer')
    preferenceID = models.ForeignKey(
        preferences, null=True, related_name='preferenceID')
    rating = models.IntegerField(default=0)


class userRelations(models.Model):
    userID = models.ForeignKey(users, related_name='userID')
    relatingUser = models.ForeignKey(users, related_name='relatingUser')
