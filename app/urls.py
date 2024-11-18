from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("/login", views.login_test, name="login"),
    path("/logout", views.user_logout, name="user_logout"),
    path("/events", views.events, name="events"),
    path("/event/<int:event_id>", views.event_detail, name="event_detail"),
    path("/add_event", views.add_event, name="add_event"),
    path("/sign_up", views.signup, name="signup"),
    path("sing_to_event/<int:event_id>", views.sign_to_event, name="sign_to_event"),
    path("sign_off_event/<int:event_id>", views.sign_off_event, name="sign_off_event"),
]
