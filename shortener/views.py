# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
import random, string, json
from shortener.models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from .forms import UrlsForm
from .utils import *

# Create your views here.
def index(request):
    data,query=searchdb(request)
    form=UrlsForm()
    return render(request,'shortener/index.html',{'title':'Url Shortener','form':form,'view':False,'data':data,'query':query})

'''def redirectOriginal(request,shortId):
    url=get_object_or_404(Urls,pk=shortId)
    url.save()
    return HttpResponseRedirect(url.httpUrl)'''

def shortenUrl(request):
    form=UrlsForm()
    if request.method=="POST":
        form=UrlsForm(request.POST)
        if form.is_valid():
            shortId=request.POST.get('shortId','')
            form.save()
            url=Urls.objects.get(shortId=shortId)
            url.shortUrl=settings.SITE_URL+"/"+shortId
            url.save()
            return redirect('/shortener/')
        return redirect('/shortener/')
    return render(request,'shortener/index.html',{"title":"Url Shortener","view":False,"form":form})

