from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm(forms.Form):
    link = forms.CharField(label="Link to image")
    desc = forms.CharField(label="Description")

# Create your views here.
def index(request):
    return render(request, "home/index.html")


def new(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data["link"]
            desc = form.cleaned_data["desc"]
            print(f"{link=}, {desc=}")
    return render(request, "home/new.html", {
        "form": NewTaskForm()
    })