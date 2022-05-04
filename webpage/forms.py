from django.forms import ModelForm, SplitDateTimeField, HiddenInput, TextInput
from django.forms.widgets import DateTimeInput, DateInput, SplitDateTimeWidget
from django.utils import timezone
from . import models
from django.utils.translation import gettext_lazy as _
# from django.contrib.gis.forms.widgets import OSMWidget

class ProfileFrom(ModelForm):
    template_name = "webpage/google_maps_form.html"
    location_fields = ['residence_location']
    class Meta:
        model = models.WorkoutProfile
        fields = ['residence_location']
        widgets = {
            'residence_location': HiddenInput() 
        }

class WSessForm(ModelForm):
    template_name = "webpage/google_maps_form.html"
    location_fields = ['location']
    
    class Meta:
        model = models.WorkoutSession
        fields = ['name', 'at', 'need_to_take', 'duration', 'description', 'location', 'how_to_contact']
        error_messages = {
            'location': {
                'required': _("Please, provide a location"),
            },
        }
        widgets = {
            'location': HiddenInput() 
        }
    at = SplitDateTimeField(label=models.WorkoutSession._meta.get_field(
        'at').verbose_name,
        help_text=models.WorkoutSession._meta.get_field(
        'at').help_text,
        widget=SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'placeholder': 'time'}), required=False)
