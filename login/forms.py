from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))