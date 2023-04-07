from django.shortcuts import render
from django.views import View

from .models import Post

# Create your views here.
class MessageView(View):
    def get(self, request):
        return render(request, "default-message.html")