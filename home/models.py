from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.TextField()

class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="users")
    image_link = models.TextField()
    description = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)