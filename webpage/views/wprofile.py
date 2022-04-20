from platform import java_ver
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
    model = models.WorkoutProfile
    form_class = forms.ProfileFrom
    
    def get_object(self):
        return get_object_or_404(self.model, user=self.request.user)
    
    def get_context_data(self, **kwargs):
        coords = utils.get_user_coords(self.request)
        ctx = super().get_context_data(**kwargs)
        ctx['y'], ctx['x'] = coords
        return ctx
    
    # def get_form(self):
    #     form = super().get_form()
    #     # utils.set_form_field_widget_to_leaflet_with_default_location(self.request, form, 'residence_location')
    #     utils.set_form_field_widget_to_google_with_default_location(self.request, form, 'residence_location')
    #     return form