from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'edit/#?$',views.edit,name='edit'),
	url(r'view/$',views.view, name='view'),	
	url(r'save/$',views.save, name='save')
]
