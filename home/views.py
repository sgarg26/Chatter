from django.shortcuts import render
from django import forms


class NewImageForm(forms.Form):
    image_link = forms.CharField(
        label="Image Link",
        widget=forms.TextInput(
            attrs={"id": "imageLink", "type": "text", "required": True}
        ),
    )
    description_input = forms.CharField(
        label="Description",
        widget=forms.TextInput(
            attrs={"id": "descriptionInput", "type": "text", "required": True}
        ),
    )


# For HW3.B we can just store our posts in memory
posts = [
    {
        "description": "A picture of space",
        "image_link": "https://source.unsplash.com/random/512x512/?space",
        "username": "krizh-p",
        "num_likes": 69,
        "comments": [
            {
                "commentUsername": "mason.george",
                "comment": "Dang, this is a great post!",
            }
        ],
        "post_id": 1,
    },
    {
        "description": "My second post!",
        "image_link": "https://source.unsplash.com/random/512x512/?smile",
        "username": "krizh-p",
        "num_likes": 1,
        "comments": [
            {
                "commentUsername": "president.washington",
                "comment": "I'm promoting you to CEO!",
            },
        ],
        "post_id": 2,
    },
]

# Create your views here.
def index(request):
    return render(request, "home/index.html", {
        "posts": posts,
        "NUM_POSTS" : len(posts)
    })


def create(request):
    if request.method == "POST":
        form = NewImageForm(request.POST)
        if form.is_valid():
            image_link = form.cleaned_data["image_link"]
            description_input = form.cleaned_data["description_input"]
            newPost = {
                "description": description_input,
                "image_link": image_link,
                "username": "krizh-p",
                "num_likes": 1,
                "comments": [],
                "post_id": len(posts) + 1,
            }
            posts.append(newPost)
    return render(request, "home/create.html", {"form": NewImageForm()})
