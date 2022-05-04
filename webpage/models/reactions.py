from django.contrib.gis.db import models
from django.urls import reverse

class InterestedInWS(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, help_text='The one who is interested in visiting the workout')
    workout = models.ForeignKey('webpage.WorkoutSession')
    
    how_to_contact = models.TextField(max_length=300)