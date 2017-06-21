from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse
from .models import Participant
from .forms import AddNewParticipant,UploadFileForm
from .utils import search,handle_uploaded_file

def home(request):
	return redirect('/register/edit/')

def save(request):
	if request.method == "POST":
		paid = request.POST.get('paid',0)
		present = request.POST.get('present',0)
		paid = True if paid is '1' else False
		present = True if present is '1' else False
		try:
			id = request.POST.get('id','')
			query = Participant.objects.get(id=id)
			query.paid = paid
			query.present = present
			query.save()
			message =  "changes for "+ query.name.lower()+ " saved"
		except:
			pass
	return HttpResponse(message);

def logout(request):
	request.session['logged'] = False
	return HttpResponseRedirect('/register/login')


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
		return render(request,'contestReg/mainView.html',
		{"title": "View", "view": True,"data": data,'q':q,'delete': True})




def view(request):

	data,q = search(request)

	return render(request,'contestReg/mainView.html',
		{"title": "View", "view": True,"data": data,'q':q})



def upload_file(request):
	if request.method == 'POST':
		print(request.FILES)
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('/register/edit/')
	else:
		form = UploadFileForm()
	return render(request, 'contestReg/forms/upload.html', {'title':'Upload','form': form})


def edit(request):

	message = request.session.get('message')
	request.session['message'] = None

	if request.method == "POST":

		form = AddNewParticipant(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('/register/edit/')
		request.session['message'] = 'Something went wrong'
		return redirect('/register/edit')
	else:
		form = AddNewParticipant()
		data,q = search(request)

		return render(request,'contestReg/mainView.html',
			{"title": "Edit", "view": False,"data": data,"form":form,'q':q,'message':message})
