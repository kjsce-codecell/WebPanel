from django.contrib import admin
from .models import Form, Question, Choice

admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Choice)