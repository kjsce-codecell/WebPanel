from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^create/$', views.create, name = 'Create'),
	url(r'^save/$', views.save, name = 'Save'),
]