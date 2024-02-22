from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")


# Create your views here.
def index(request):
    return render(request, "home/index.html")


def new(request):
    return render(request, "home/new.html")