from django.urls import path

from . import views  # from django_notepad import views

urlpatterns = [
    path("", views.home, name=""),
    path("index/", views.index, name="index"),
]
