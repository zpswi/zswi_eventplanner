from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from app.forms import AddEventForm

def index(request):
    html = render(request, "app/index.html")
    return HttpResponse(html)


def add_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Created new event")

    return HttpResponseRedirect(reverse('index'))