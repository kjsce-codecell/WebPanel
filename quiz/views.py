# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Week, Question, Option

# Create your views here.

def index(request):
	data = []
	week_no = Week.objects.count();
	questions = []
	try:
		questions = Question.objects.filter(week = Week.objects.last())
	except:
		pass
	for index, q in enumerate(questions):
		options = []
		for o in Option.objects.filter(question = q.id):
			options.append(o.choice)
		data.append({"no": index+1, "question": q.question, "options": options})
	return render(request, 'quiz/index.html', {"title": "Quiz", "data": data, "quiz": True, "week": week_no})

def success(request):
	if request.method == 'POST':
		c = [request.POST.get('1', "#!null"), request.POST.get('2', "#!null")]
		questions = []
		points = 0
		try:
			questions = Question.objects.filter(week = Week.objects.last())
		except:
			pass
		for i, q in enumerate(questions):
			if(c[i] == q.option_set.filter(ans = True)[0].choice):
				points = points + 1
		message = "Results are saved, "+str(points)+" points added.<br>Your total is: 103<br>Answers wil be displayed by the end of the week.<br>Your choices are mailed to you.<br>"
		return render(request, 'quiz/index.html', {"title": "Done", "message": message, "quiz": False})
	else:
		return redirect('/quiz/')