from django.shortcuts import render
from .models import *

# Create your views here.
def user(request, a):
    data = {
        "user": CustomUser.objects.get(id=a),
    }
    return render("friens-lists.html", data)