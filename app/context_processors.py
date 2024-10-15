from app.forms import AddEventForm


def add_event_form(request):
    return {'add_event_form': AddEventForm()}