from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from webpage import forms
from django.contrib.gis.geoip2 import geoip2
from . import utils
from django.contrib.gis.geos import Point
from webpage import models
from django.shortcuts import get_object_or_404
from django.contrib.gis.forms.widgets import OSMWidget

class WProfileUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'webpage/workoutprofile_form.html'
    model = models.WorkoutProfile
    fields = ['residence_location']
    
    def get_object(self):
        return get_object_or_404(self.model, user=self.request.user)
    
    def get_form(self):
        form = super().get_form()
        try:
            (lat, lon) = utils.get_user_coords(self.request)
            osmw = OSMWidget(attrs={'default_lat': lat, 'default_lon': lon, 'geom_type': 'POINT'})
        except geoip2.errors.AddressNotFoundError:
            osmw = OSMWidget(attrs={'geom_type': 'POINT'})
        form.fields['residence_location'].widget = osmw
        return form