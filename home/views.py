from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

curr_id = 2

# Create your views here.
posts = [
    {
        "link": "https://images.pexels.com/photos/20413769/pexels-photo-20413769/free-photo-of-a-black-and-white-photo-of-a-swan-in-the-water.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        "desc": "Picture of swan",
        "uname": "u1",
        # "num_likes": 12,
        # "comments": [
        #     {
        #         "commentUserName": "u2",
        #         "comment": "Nice post",
        #     },
        # ],
        "post_id": 2,
    },
    {
        "link": "https://images.pexels.com/photos/20416961/pexels-photo-20416961/free-photo-of-street-photography.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        "desc": "Picture of restaurant",
        "uname": "Person2",
        "post_id": 1,
    },
]


class NewForm(forms.Form):
    link = forms.CharField(label="Link to image")
    desc = forms.CharField(label="Description")
    uname = forms.CharField(label="Username")
    profile_pic = forms.CharField(label="Profile Picture")


def index(request):
    return render(request, "home/index.html", {"posts": posts})


def print_posts():
    for i, post in enumerate(posts):
        print(f"i:{i}")
        print(f"link: {post['link']} desc: {post['desc']}")


def create(request):
    if request.method == "POST":
        print("request POST")
        form = NewForm(request.POST)
        if form.is_valid():
            print("form is valid")
            link = form.cleaned_data["link"]
            desc = form.cleaned_data["desc"]
            uname = form.cleaned_data["uname"]
            profile_pic = form.cleaned_data["profile_pic"]
            curr_id += 1
            new_post = {
                "link": link,
                "desc": desc,
                "uname": uname,
                "profile_pic": profile_pic,
                "post_id": curr_id
            }
            posts.insert(0, new_post)
        return HttpResponseRedirect(reverse("home:index"))
    print("request not post")
    return render(request, "home/create.html", {"form": NewForm()})
