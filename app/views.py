from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app.forms import AddEventForm

def index(request):
    html = render(request, "app/index.html")
    return HttpResponse(html)


@login_required
def login_test(request):
    return render(request, "app/index.html")



def add_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Created new event")

    return HttpResponseRedirect(reverse('index'))