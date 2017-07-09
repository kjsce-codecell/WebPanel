from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .models import Form, Question, Choice

def fill(request, id):
	form = {}
	f = Form.objects.all().filter(id = id)
	try:
		form['name'] = f[0].name
		form['id'] = f[0].id
	except:
		return redirect('/home')
	q_set = f[0].question_set.all()
	form['questions'] = []
	for i,q in enumerate(q_set):
		question = {}
		question['text'] = q.q_text
		question['type'] = q.q_type
		question['no'] = i+1
		if q.q_type is not 1:
			question['choices'] = []
			ch = q.choice_set.all()
			for choice in ch:
				question['choices'].append(choice.c_text)
		form['questions'].append(question)
	return render(request, 'feedbackform/index.html', {"title": "Fill Form", "fillForm": True, "data": form})

def submit(request):
	if request.method == "POST":
		f = []
		try:
			f = Form.objects.all().get(id = request.POST.get('id', 0))
		except:
			return HttpResponse("Error: Form Doesn't Exist")
		for i in range (f.question_set.all().count()):
			if not (request.POST.get(str(i+1), '-1') == '-1' or request.POST.get(str(i+1), '-1') == ''):
				c = f.question_set.all()[i].choice_set.filter(c_text = request.POST.get(str(i+1), '-1'))
				if len(c) == 1:
					c[0].c_count = c[0].c_count + 1
					c[0].save()
				else:
					f.question_set.all()[i].choice_set.create(c_text = request.POST.get(str(i+1), '-1'), c_count = 1)
		return HttpResponse("Success")
	else:
		return redirect("/home/")

def save(request):
	if request.method == "POST":
		data = json.loads(request.POST.get('save'))
		formObj = Form(name = data['Name'])
		formObj.save()
		for q in data['data']:
			questionObj = Question(q_text = q['name'], q_type = q['type'], form = formObj)
			questionObj.save()
			if 'choices' in q:
				for c in q['choices']:
					Choice(c_text = c, question = questionObj).save()
		return HttpResponse("Saved")
	else:
		return redirect('/home/')

def create(request):
	return render(request, 'feedbackform/index.html', {"title": "Make Form", "create": True})
