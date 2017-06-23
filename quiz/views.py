# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Week, Question, Option, User, Points
from django.db.models import Sum

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
		w = Week.objects.last()
		if User.objects.filter(rollNo = int(request.POST.get("RollNo", 0))).count() != 1:
			User(rollNo = int(request.POST.get("RollNo", 0)), name = request.POST.get("Name", "#!null"), email = request.POST.get("Email", "#!null")).save()
		user = User.objects.get(rollNo = int(request.POST.get("RollNo", 0)))
		questions = []
		points = 0
		try:
			questions = Question.objects.filter(week = w)
		except:
			pass
		for i, q in enumerate(questions):
			c = request.POST.get(str(i+1), "#!null")
			if(c == q.option_set.filter(ans = True)[0].choice):
				points = points + 1
		if Points.objects.filter(user = user, week = w).count() == 0:
			Points.objects.create(user = user, week = w, point = points)
			total = Points.objects.filter(user = user).annotate(num = Sum('point'))[0].num
			message = "Results are saved, "+str(points)+" points added.<br>Your total is: "+str(total)+"<br>Answers wil be displayed by the end of the week.<br>Your choices are mailed to you.<br>"
			return render(request, 'quiz/index.html', {"title": "Done", "message": message, "quiz": False})
		else:
			message = "You have already submitted for this quiz."
			return render(request, 'quiz/index.html', {"title": "Done", "failure": message, "quiz": False})
	else:
		return redirect('/quiz/')

def weeks(request):
	weeks = Week.objects.values_list('id', flat = True)
	return render(request, 'quiz/index.html', {"title": "All Quizs", "data": weeks, "weeks":True})

def ranks(request, week):
	data = []
	point = Points.objects.filter(week = week)
	for i,p in enumerate(point):
		data.append({"rank": (i+1),"name": p.user.name, "points": str(p.point), "rollNo": str(p.user.rollNo)})
	return render(request, 'quiz/index.html', {"title": "Ranks", "data": data, "ranks": True, "week": week})