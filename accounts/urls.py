from django.urls import path
from .views import *

urlpatterns = [
    path("user/<str:a>/", user),
    path("users/", users, name="users"),
    path('follow/', follow, name='follow'),
    path("login/", login_user, name="login"),
    path("register/", signup, name="register")
]
