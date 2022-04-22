from accounts.models import CustomUser
from django.contrib.gis.db import models
from django.urls import reverse

class WorkoutProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    residence_location = models.PointField(spatial_index=True, geography=True, null=True, blank=True, help_text='Select the location around which it\'s the most convenient for you to work out on a regular basis. Leave it out, if you can\'t remain at one place for a long time. This info will help your neighbors to find you, and doesn\'t restrict you from visiting more distant locations or posting training session invitations elsewhere.')
    
    def __str__(self) -> str:
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.user.id})
    