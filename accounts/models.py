from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    about = models.TextField(null=True)
    country = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to="profile", null=True)
    followers = models.ManyToManyField(User, related_name="followers", null=True, blank=True)

class Follow(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    followers = models.ManyToManyField(CustomUser, related_name="follower", null=True, blank=True)