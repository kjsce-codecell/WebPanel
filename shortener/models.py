# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

class Urls(models.Model):
    name=models.CharField(max_length=200)
    shortId=models.CharField(max_length=7,primary_key=True)
    httpUrl=models.URLField(max_length=200)
    shortUrl=models.URLField(max_length=100)

# Create your models here.
