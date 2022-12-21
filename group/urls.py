from django.urls import path

from .views import GroupView


urlpatterns = [
    path("groups/", GroupView.as_view(), name="groups")
]
