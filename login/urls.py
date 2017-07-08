from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'login/', views.login, name = 'login'),
	url(r'home/$',views.home, name='home'),
	url(r'logout/$',views.logout,name='logout'),
]
