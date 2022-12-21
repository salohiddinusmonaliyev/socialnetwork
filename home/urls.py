from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("addlike/", AddLikeView.as_view(), name="addlike"),
    path("adddislike/", AddDislikeView.as_view(), name="adddislike"),
]
