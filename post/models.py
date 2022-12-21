from django.db import models

from accounts.models import CustomUser

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    file = models.FileField(upload_to=None, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(CustomUser, null=True, blank=True, related_name="liked")
    disliked = models.ManyToManyField(CustomUser, null=True, blank=True, related_name="disliked")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    @property
    def liked_count(self):
        return self.liked.all.count()

    def __str__(self):
        return self.author.username

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
