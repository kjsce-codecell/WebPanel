from django.db import models

# Create your models here.

class Form(models.Model):
	name = models.CharField(max_length = 300, unique = True)

class Question(models.Model):
	q_text = models.CharField(max_length = 300)
	q_type = models.PositiveSmallIntegerField()
	form = models.ForeignKey(Form, on_delete = models.CASCADE)
	class Meta:
		unique_together = ('q_text', 'form',)

class Choice(models.Model):
	c_text = models.CharField(max_length = 300)
	c_count = models.PositiveSmallIntegerField(default = 0)
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	class Meta:
		unique_together = ('c_text', 'question',)