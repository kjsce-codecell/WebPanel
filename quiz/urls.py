from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'Index'),
	url(r'^save/$', views.success, name = 'Success'),
	url(r'^ranklist/$', views.weeks, name = "Weeks"),
	url(r'^ranklist/week(?P<week>[0-9]+)/$', views.ranks, name = 'Ranks'),
]