from django.urls import path


from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("addlike/<int:pk>/", AddLikeView.as_view()),
    path("adddislike/", AddDislikeView.as_view(), name="adddislike"),
]
