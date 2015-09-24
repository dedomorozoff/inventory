# Create your views here.
from django.http import HttpResponse
from django import forms
from django.shortcuts import render
from showbase.models import Podotchet
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
def index(request):
    form = ContactForm()
    return render(request,'index.html',{'form': form,})
