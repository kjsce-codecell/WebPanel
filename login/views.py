from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import LoginForm
from .models import Login

# Create your views here.
def login(request):
	if request.session.get('logged', False) == True:
		return redirect('/home')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		try:
			query = Login.objects.get(username = username)
			
			if query.password == password:
				request.session['message'] = ''
				request.session['logged'] = True
				return redirect('/home')
			request.session['message'] = "Invalid password or username"
		except:
			request.session['message'] = "Invalid password or username"
			return redirect('/login')
	message = ''
	if('message' in request.session):
		message= request.session['message']
	forms = LoginForm()

	return render(request, 'login/login.html',{"message":message,"title": "Login","forms": forms })


def home(request):
	return render(request,'login/landing_page.html',{"title": "Home"})


def logout(request):
	request.session['logged'] = False
	return HttpResponseRedirect('/login')