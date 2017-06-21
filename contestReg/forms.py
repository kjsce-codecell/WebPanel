from django import forms
from .models import Participant

class AddNewParticipant(forms.ModelForm):
	class Meta():
		model = Participant
		fields = '__all__'
		widgets = {
		"name" : forms.TextInput(attrs={'class':'form-control '}),
		"email": forms.EmailInput(attrs={'class':'form-control '}),
		"college": forms.TextInput(attrs={'class':'form-control margin-bottom'}),
		"number": forms.TextInput(attrs={'class':'form-control '}),
		"paid": forms.CheckboxInput(attrs={'class':''})
		# "": form.TextInput('class': 'form-control'),
		
		}

	# name    = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	# email   = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	# number  = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	# college = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	# paid    = forms.BooleanField(required=True)
	# present = forms.BooleanField(required=True)

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length="50",widget=forms.TextInput(attrs={'class':'form-control'}))
	file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
