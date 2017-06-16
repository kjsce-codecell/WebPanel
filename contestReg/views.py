from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Participant
from .forms import AddNewParticipant


def save(request):
	if request.method == "POST":
		paid = request.POST.get('paid','')
		present = request.POST.get('present','')
		paid = False if paid is '' else True
		present = False if present is '' else True
		id = request.POST.get('id','')
		query = Participant.objects.get(id=id)
		query.paid = paid
		query.present = present
		query.save()
	return redirect('/register/edit/')



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
	print(request.method)
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
			{"title": "Chaitya Shah", "view": False,"data": data,"form":form,'q':q})


# Create your views here.
