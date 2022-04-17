from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from timezone_field import TimeZoneField
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    tz = TimeZoneField(default="UTC")
    phone_number = models.CharField(max_length=50, blank=True)
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={"pk": self.pk})
