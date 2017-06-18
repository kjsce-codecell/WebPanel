from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from .models import Participant
from .forms import AddNewParticipant

def home(request):
	return redirect('/register/edit/')

def save(request):
	# subject to change

	if request.method == "POST":
		paid = request.POST.get('paid',0)
		present = request.POST.get('present',0)
		paid = True if paid is  '1' else False
		present = True if present is '1' else False
		try:
			id = request.POST.get('id','')
			query = Participant.objects.get(id=id)
			# print(paid)
			# print(present)
			query.paid = paid
			query.present = present
			query.save()
			message =  "changes for "+ query.name.lower()+ " saved"
		except:
			pass
	return HttpResponse(message);

def delete(request):
	if request.method == "POST":
		id = request.POST.get('id',0)
		try:
			query = Participant.objects.get(id=id);
			query.delete();
		except:
			pass
		return redirect('/register/delete/')
	else:
		q = request.GET.get('q','')
		if q is not '':
			data = Participant.objects.filter(name__startswith = q);
		else:
			data = Participant.objects.all();
		return render(request,'contestReg/edit.html',
		{"title": "View", "view": True,"data": data,'q':q,'delete': True})

def view(request):
	#print(request)
	data = Participant.objects.all();
	data = None
	q = request.GET.get('q','')
	if q is not '':
		data = Participant.objects.filter(name__startswith = q);
	else:
		data = Participant.objects.all();
	#template = get_template('contestReg/index.html')
	return render(request,'contestReg/edit.html',
		{"title": "View", "view": True,"data": data,'q':q})

def edit(request):
	message = request.session.get('message')
	request.session['message'] = None
	#print(request)
	if request.method == "POST":
		form = AddNewParticipant(data = request.POST)

		if form.is_valid():
			form.save()
			return redirect('/register/edit/')
	else:
		form = AddNewParticipant()
		q = request.GET.get('q','')
		data = None
		if q is not '':
			data = Participant.objects.filter(name__startswith = q);
		else:
			data = Participant.objects.all();
		#template = get_template('contestReg/index.html')
		return render(request,'contestReg/edit.html',
			{"title": "Edit", "view": False,"data": data,"form":form,'q':q,'message':message})

# Create your views here.