from django.contrib.gis import admin
# from leaflet.admin import LeafletGeoAdmin
from . import models

# admin.site.register(models.WorkoutProfile, LeafletGeoAdmin)
# admin.site.register(models.WorkoutSession, LeafletGeoAdmin)

admin.site.register(models.WorkoutProfile)
admin.site.register(models.WorkoutSession)
