from django.conf.urls import * 
from . import views
urlpatterns=[
        url(r'^$',views.index,name='index'),
        #url(r'^(?P<shortId>[-\w]{1,7})$',views.redirectOriginal,name='redirectOriginal'),
        url(r'^shortenUrl/$',views.shortenUrl,name='shortenUrl'),
       ] 
