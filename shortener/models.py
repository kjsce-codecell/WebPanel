# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

class Urls(models.Model):
    shortId=models.SlugField(max_length=7,primary_key=True)
    httpUrl=models.URLField(max_length=200)
    timeStamp=models.DateTimeField(auto_now=True)

def __str__(self):
    return self.httpUrl
# Create your models here.
