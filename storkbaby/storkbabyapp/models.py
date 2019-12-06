# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class pup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='profilepics')
    description = models.CharField(max_length=250)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)
