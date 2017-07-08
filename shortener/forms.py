from django import forms
from .models import Urls
from django.forms import ModelForm

class UrlsForm(ModelForm):
    class Meta():
        model=Urls
        fields=['name','httpUrl','shortId']

        labels={
                "name":"Workshop Name",
                "httpUrl":"Original Url",
                "shortId":"Workshop Code"
                }

        widgets={
                "httpUrl":forms.TextInput(attrs={'class':'form-control','placeholder':'https://www.codechef.com/'}),
                "shortId":forms.TextInput(attrs={'class':'form-control','placeholder':'cchef'}),
                "name":forms.TextInput(attrs={'class':'form-control','placeholder':'Intro to CP'}),
                }


