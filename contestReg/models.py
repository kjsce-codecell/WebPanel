from django.db import models

class Participant(models.Model):
	name    = models.CharField(max_length = 250)
	email   = models.EmailField(max_length = 250)
	number  = models.CharField(max_length = 15)
	college = models.CharField(max_length = 250)
	paid    = models.BooleanField(default = False)
	present = models.BooleanField(default = False)

	def __str__(self):
		return self.name

class LoginModel(models.Model):
	username = models.CharField(max_length=250)
	password = models.CharField(max_length=250)