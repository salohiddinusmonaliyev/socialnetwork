from django.db import models
from django.urls import reverse

from accounts.models import CustomUser

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    file = models.FileField(upload_to=None, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(CustomUser, blank=True, related_name="liked")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    @property
    def liked_count(self):
        return self.liked.all.count()

    def __str__(self):
        return self.author.user.username
    
    def get_absolute_url(self):
        return reverse("home")
    

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.post

class Short(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Chat(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user2")
    def __str__(self):
        return f"{self.user1} {self.user2}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="chat")
    message = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="author")
    to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="to")
    date = models.DateTimeField(auto_now_add=True)