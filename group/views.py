from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.
class GroupView(View):
    def get(self, request):
        data = {
            "groups": Group.objects.all(),
        }
        return render(request, 'groups.html', data)