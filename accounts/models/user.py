from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
