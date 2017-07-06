from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .models import Form, Question, Choice

# Create your views here.
def index(request):
	return HttpResponse("Hello World")

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