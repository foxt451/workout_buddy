from django.contrib.gis import admin
from . import models

admin.site.register(models.WorkoutProfile, admin.GISModelAdmin)
admin.site.register(models.WorkoutSession)
