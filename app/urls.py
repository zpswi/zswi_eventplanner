#create simple 
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("/add_event", views.add_event, name="add_event"),
]