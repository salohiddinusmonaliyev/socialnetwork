from django.shortcuts import render

from post.models import Post
from .models import *

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User


# Create your views here.
def user(request, a):
    user = CustomUser.objects.get(username=a).id
    data = {
        "user": CustomUser.objects.get(username=a),
        "posts": Post.objects.filter(author_id=user),
    }
    return render(request, "user-page.html", data)

def users(request):
    context = {
        "users":CustomUser.objects.all(),
        "author":CustomUser.objects.get(user=request.user),
    }
    return render(request, "default-member.html", context)

from django.shortcuts import get_object_or_404, render

from post.models import Post
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def follow(request):
    if request.method == "POST":
        username = request.POST.get("follow")

        username1 = username.split(", ")[1]
        username0 = username.split(", ")[0]
        if username0=="follow":
            user11 = User.objects.get(username=username1)

            user = get_object_or_404(CustomUser, user_id=user11.id)
            
            if user.id != request.user.id:
                user.followers.add(request.user)
        else:
            user11 = User.objects.get(username=username1)
            user = get_object_or_404(CustomUser, user_id=user11.id)
            
            if user.id != request.user.id:
                user.followers.remove(request.user)

        return redirect('users')
    
    


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Foydalanuvchi kirdi va boshqa sahifaga o'tkazish
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        image = request.POST.get("image")
        user = User.objects.create_user(username, email, password)
        user.save()
        CustomUser.objects.create(user=user, first_name=first_name, last_name=last_name, email=email, image=image)
        return redirect("/login/")
    else:
        return render(request, 'register.html')

