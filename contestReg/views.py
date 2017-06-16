from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

data = [
		{
		"name": "Chaitya Shah",
		"email": "chaitya.shah@somaiya.edu",
		"number": "9029168990",
		"paid": True,
		"present": False,
		},
		{
		"name": "Priyansh Shah",
		"email": "p.shah@somaiya.edu",
		"number": "8022128590",
		"paid": False,
		"present": False
		},
		{
		"name": "Chaya Sawla",
		"email": "ch.sw@somaiya.edu",
		"number": "9049062940",
		"paid": False,
		"present": False
		},
	];


def view(request):
	#print(request)
	
	#template = get_template('contestReg/index.html')
	return render(request,'contestReg/edit.html',
		{"title": "Chaitya Shah", "view": True,"data": data})

def edit(request):
	#print(request)
	
	#template = get_template('contestReg/index.html')
	return render(request,'contestReg/edit.html',
		{"title": "Chaitya Shah", "view": False,"data": data})


# Create your views here.
