# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Week(models.Model):
	pass

class Question(models.Model):
	question = models.CharField(max_length = 300)
	week = models.ForeignKey(Week, on_delete = models.CASCADE)

class Option(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice = models.CharField(max_length = 300)
	ans = models.BooleanField(default = False)

class User(models.Model):
	rollNo = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	email = models.CharField(max_length = 256)
	week = models.ManyToManyField(Week, through = 'Points')

class Points(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	week = models.ForeignKey(Week, on_delete = models.CASCADE)
	point = models.IntegerField()
	class Meta:
		ordering = ['-point']