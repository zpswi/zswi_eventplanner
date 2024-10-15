
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("/login", views.login_test, name="login"),
    path("/add_event", views.add_event, name="add_event"),
]