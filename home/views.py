from django.shortcuts import redirect, render
from django.views import View

from post.models import *

# Create your views here.
class HomeView(View):
    def get(self, request):
        data = {
            "post": Post.objects.all(),
            "user": request.user,
            "all_user": CustomUser.objects.all,
        }
        return render(request, "index.html", data)

class AddLikeView(View):
    def post(self, request):
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        if request.user in post.liked.all():
            post.liked.remove(request.user)
        else:
            if request.user in post.disliked.all():
                post.disliked.remove(request.user)
                post.liked.add(request.user)
            else:
                post.liked.add(request.user)
        return redirect('/')

class AddDislikeView(View):
    def post(self, request):
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        if request.user in post.disliked.all():
            post.disliked.remove(request.user)
        else:
            if request.user in post.liked.all():
                post.liked.remove(request.user)
                post.disliked.add(request.user)
            else:
                post.disliked.add(request.user)
        return redirect('/')