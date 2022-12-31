from django.urls import path
from .views import *

urlpatterns = [
    path("user/<int:a>/", user),
]
