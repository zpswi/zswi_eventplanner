from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from app.forms import AddEventForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from app.models import Event
from django.contrib.auth import logout
from .forms import EventFilterForm
from django.core import serializers


def index(request):
    html = render(request, "app/index.html")
    return HttpResponse(html)


@login_required
def login_test(request):
    return render(request, "app/index.html")

@login_required
def add_event(request):
    if request.method == "POST":
        form = AddEventForm(request.POST)
        form.instance.user = request.user

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Created new event")

    return HttpResponseRedirect(reverse("index"))


def events(request):
    form = EventFilterForm(request.GET)
    events = Event.objects.all()

    if form.is_valid():
        if form.cleaned_data["title"]:
            events = events.filter(title__icontains=form.cleaned_data["title"])
        if form.cleaned_data["location"]:
            events = events.filter(location__icontains=form.cleaned_data["location"])
        if form.cleaned_data["start_time_after"]:
            events = events.filter(
                start_time__gte=form.cleaned_data["start_time_after"]
            )
        if form.cleaned_data["end_time_before"]:
            events = events.filter(end_time__lte=form.cleaned_data["end_time_before"])
        if form.cleaned_data["all_day_select"] != "":
            events = events.filter(all_day=form.cleaned_data["all_day_select"])

    return render(request, "events/list.html", {"events": events, "form": form})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, "events/detail.html", {
        "event": event,
        "signed_up": request.user in event.participants.all(),
    })

@login_required
def my_events(request):
    data = serializers.serialize('json', Event.objects.filter(user=request.user.id))
    return render(request, "events/my_events.html", {'events': data})


@login_required
def user_logout(request):
    logout(request)
    return render(request, "user/logout.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def sign_to_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if event.participants.count() >= event.capacity:
        messages.add_message(request, messages.ERROR, "Event is full")
        return HttpResponseRedirect(reverse("event_detail", args=[event_id]))
    if request.user in event.participants.all():
        messages.add_message(request, messages.ERROR, "You are already signed up")
        return HttpResponseRedirect(reverse("event_detail", args=[event_id]))
    event.participants.add(request.user)
    messages.add_message(request, messages.SUCCESS, "Signed up")
    return HttpResponseRedirect(reverse("event_detail", args=[event_id]))


@login_required
def sign_off_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.user not in event.participants.all():
        messages.add_message(request, messages.ERROR, "You are not signed up")
        return HttpResponseRedirect(reverse("event_detail", args=[event_id]))
    event.participants.remove(request.user)
    messages.add_message(request, messages.SUCCESS, "Signed off")
    return HttpResponseRedirect(reverse("event_detail", args=[event_id]))

@login_required
def remove_user_from_event(request, event_id, removed_user_id):
    event = Event.objects.get(id=event_id)

    if request.user != event.user:
        return HttpResponseRedirect(reverse("event_detail", args=[event_id]))

    event.participants.remove(removed_user_id)
    messages.add_message(request, messages.SUCCESS, "User removed")

    return HttpResponseRedirect(reverse("event_detail", args=[event_id]))
