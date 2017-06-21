# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
	message = 'Hello, Quiz';
	try:
		if request.session['logged'] == True:
			return render(request, 'quiz/index.html', {"message": message, "title": "Quiz"});
	except:
		return redirect('/quiz/login')
	return redirect('/quiz/login')