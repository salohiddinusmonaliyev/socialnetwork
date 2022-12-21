from django.db import models

from accounts.models import CustomUser

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='groups/', null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GroupItem(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.group.name
