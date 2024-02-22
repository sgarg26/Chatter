from django import forms
from django.shortcuts import render


class NewTaskForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")


# Create your views here.
def index(request):
    return render(request, "home/index.html")


def new(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            new_post = {"title": title, "content": content}

