from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
posts = [
    {
        "link": "https://images.pexels.com/photos/20413769/pexels-photo-20413769/free-photo-of-a-black-and-white-photo-of-a-swan-in-the-water.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        "desc": "Picture of swan",
    },
    {
        "link": "https://images.pexels.com/photos/20416961/pexels-photo-20416961/free-photo-of-street-photography.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        "desc": "Picture of restaurant",
    },
]


class NewForm(forms.Form):
    link = forms.CharField(label="Link to image")
    desc = forms.CharField(label="Description")


def index(request):
    return render(request, "home/index.html")


def create(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data["link"]
            desc = form.cleaned_data["desc"]
            new_post = {"link": link, "desc": desc}
            posts.insert(0, new_post)
            print("donezo")
        return HttpResponseRedirect(reverse("home:create"))
    return render(request, "home/create.html", {"form": NewForm()})
    # return render(request, "home/create.html")

