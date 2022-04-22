from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinLengthValidator
from django.contrib.gis.db import models
from django.urls import reverse

class WorkoutSession(models.Model):
    name = models.CharField(max_length=255, help_text="Give it a name", validators=[MinLengthValidator(3)])
    location = models.PointField(help_text='Where the workout will take place or start. Defaults to your current location', geography=True, spatial_index=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    at = models.DateTimeField('Date and time', blank=True, null=True, help_text='When your workout will take place. If it\'s a regular activity, leave this field empty and specify the regularity in the description.')
    need_to_take = models.TextField(max_length=500, blank=True, help_text='What people should take with them')
    duration = models.PositiveIntegerField('Duration in minutes', blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, help_text='All people need to now about this workout that hasn\'t yet been specified (like specific time or prerequisits...)')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Session at {self.at or 'an undefined time'}"
    
    def get_absolute_url(self):
        return reverse('webpage:wsess-detail', kwargs={"pk": self.id})
    