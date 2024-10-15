from .models import Event
from django import forms

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'participants', 'capacity', 'description', 'location', 'start_time', 'end_time', 'all_day']

    def __init__(self, *args, **kwargs):
        super(AddEventForm, self).__init__(*args, **kwargs)
        self.fields['participants'].required = False