from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

curr_id = 2


def get_set_curr_id():
    global curr_id
    curr_id += 1
    return curr_id

# Create your views here.
posts = [
    {
        "link": "https://images.pexels.com/photos/20413769/pexels-photo-20413769/free-photo-of-a-black-and-white-photo-of-a-swan-in-the-water.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        "desc": "Picture of swan",
        "uname": "u1",
        "num_likes": 12,
        "post_id": 2,
        "profile_pic": "https://images.pexels.com/photos/20464951/pexels-photo-20464951/free-photo-of-a-silhouette-of-a-person-riding-a-camel-in-the-desert.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
    },
    {
        "link": "https://images.pexels.com/photos/20416961/pexels-photo-20416961/free-photo-of-street-photography.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        "desc": "Picture of restaurant",
        "uname": "Person2",
        "post_id": 1,
        "num_likes": 5,
        "profile_pic": "https://images.pexels.com/photos/18149314/pexels-photo-18149314/free-photo-of-woman-sitting-on-boat.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
    },
]


class NewForm(forms.Form):
    link = forms.CharField(label="Link to image")
    desc = forms.CharField(label="Description")
    uname = forms.CharField(label="Username")
    num_likes = forms.CharField(label="Number of likes")
    profile_pic = forms.CharField(label="Profile Picture")


def index(request):
    return render(request, "home/index.html", {"posts": posts})


def create(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data["link"]
            desc = form.cleaned_data["desc"]
            uname = form.cleaned_data["uname"]
            num_likes = form.cleaned_data["num_likes"]
            profile_pic = form.cleaned_data["profile_pic"]
            new_post = {
                "link": link,
                "desc": desc,
                "uname": uname,
                "profile_pic": profile_pic,
                "post_id": get_set_curr_id(),
                "num_likes": num_likes
            }
            posts.insert(0, new_post)
        return HttpResponseRedirect(reverse("home:index"))
    return render(request, "home/create.html", {"form": NewForm()})
