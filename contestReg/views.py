from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Participant
from .forms import AddNewParticipant


def save(request):
	# subject to change

	if request.method == "POST":
		paid = request.POST.get('paid',0)
		present = request.POST.get('present',0)
		paid = True if paid is  '1' else False
		present = True if present is '1' else False
		id = request.POST.get('id','')
		query = Participant.objects.get(id=id)
		# print(paid)
		# print(present)
		query.paid = paid
		query.present = present
		query.save()
		message =  "changes for "+ query.name.lower()+ " saved"
	return HttpResponse(message);



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
		{"title": "Chaitya Shah", "view": True,"data": data,'q':q})

def edit(request):

	message = request.session.get('message')
	request.session['message'] = None
	#print(request)

	if request.method == "POST":
		form = AddNewParticipant(data = request.POST)

		if form.is_valid():
			form.save()
			return redirect('/register/view')
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
			{"title": "Chaitya Shah", "view": False,"data": data,"form":form,'q':q,'message':message})


# Create your views here.
