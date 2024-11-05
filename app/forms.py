from .models import Event
from django import forms


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "participants",
            "capacity",
            "description",
            "location",
            "start_time",
            "end_time",
            "all_day",
        ]
        widgets = {
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        super(AddEventForm, self).__init__(*args, **kwargs)
        self.fields["participants"].required = False


class EventFilterForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=False,
        label="Title",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )
    location = forms.CharField(
        max_length=255,
        required=False,
        label="Location",
        widget=forms.TextInput(attrs={"placeholder": "Search by location"}),
    )
    start_time_after = forms.DateTimeField(
        required=False,
        label="Start Time After",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )
    end_time_before = forms.DateTimeField(
        required=False,
        label="End Time Before",
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )
    
    all_day_select = forms.ChoiceField(
        required=False,
        label="Type of event",
        choices=[(None, "All events"), (True, "All day events"), (False, "Non all day events")],
    )
