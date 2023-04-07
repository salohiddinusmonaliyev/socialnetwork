from django.shortcuts import redirect, render
from django.views import View

from django.http import HttpResponseRedirect

from post.models import *

# Create your views here.
class HomeView(View):
    def get(self, request):
        data = {
            "post": Post.objects.all(),
            "user": CustomUser.objects.get(user=request.user),
            "all_user": CustomUser.objects.all(),
        }
        return render(request, "default.html", data)

class AddLikeView(View):
    def get(self, request, pk):
        post_id = pk
        post = Post.objects.get(id=post_id)
        r_user = request.user
        user = CustomUser.objects.get(user=r_user)
        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)
        return HttpResponseRedirect(reverse('home'))

class LikeView(View):
    def get(self, request, pk):
        post_id = pk
        post = Post.objects.get(id=post_id)
        
        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)
        return HttpResponseRedirect(reverse('user'))


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