from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^create/$', views.create, name = 'Create'),
	url(r'^save/$', views.save, name = 'Save'),
	url(r'^form(?P<id>[0-9]+)/$', views.fill, name = 'Fill'),
	url(r'^submit/$', views.submit, name = 'Submit'),