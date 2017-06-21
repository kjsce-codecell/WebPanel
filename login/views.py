from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import Login

# Create your views here.
def index(request):
	if request.session['logged'] != True:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			#print(password)
			try:
				query = Login.objects.get(username = username)
				#print(query.password)
				if query.password == password:
					request.session['message'] = ''
					request.session['logged'] = True
					return redirect('/register')
				request.session['message'] = "Invalid password or username"
			except:
				request.session['message'] = "Invalid password or username"
				return redirect('/login')
		message = ''
		if('message' in request.session):
			message= request.session['message']
		forms = LoginForm()

		return render(request, 'login/login.html',{"message":message,"title": "Login","forms": forms })
	else:
		return redirect('/quiz')