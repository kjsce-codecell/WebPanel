from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'login/', views.login, name = 'login'),
	url(r'home/$',views.home, name='home'),
	url(r'logout/$',views.logout,name='logout'),
    url(r'^(?!admin|home|login|home|logout)(?P<shortId>[-\w]{1,7})$',views.redirectOriginal,name='redirectOriginal'),
]
