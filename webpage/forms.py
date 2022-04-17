from django.forms import ModelForm, SplitDateTimeField
from django.forms.widgets import DateTimeInput, DateInput, SplitDateTimeWidget
from django.utils import timezone
from . import models
# from django.contrib.gis.forms.widgets import OSMWidget

# class ProfileFrom(ModelForm):
#     class Meta:
#         model = models.WorkoutProfile
#         fields = ['residence_location']
#         widgets = {
#             'residence_location': OSMWidget,
#         }


class WSessForm(ModelForm):
    class Meta:
        model = models.WorkoutSession
        fields = ['name', 'at', 'need_to_take', 'duration', 'description']
        widgets = {
            #'at': DateInput(attrs={'type': 'date'})
        }
    at = SplitDateTimeField(label=models.WorkoutSession._meta.get_field(
        'at').verbose_name,
        help_text=models.WorkoutSession._meta.get_field(
        'at').help_text,
        widget=SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'placeholder': 'time'}), required=False)
