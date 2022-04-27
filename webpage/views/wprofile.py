
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from webpage import forms

from django.contrib.gis.geoip2 import geoip2
from . import utils
from django.db.models.functions import Concat
from django.contrib.gis.geos import Point
from webpage import models
from django.db.models import F, Value
from django.shortcuts import get_object_or_404, render
from django.contrib.gis.forms.widgets import OSMWidget
from django.contrib.gis.db.models.functions import Distance

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
    
class WProfileCreate(LoginRequiredMixin, CreateView):
    model = models.WorkoutProfile
    form_class = forms.ProfileFrom
    
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'workoutprofile'):
            return render(request, 'webpage/user_has_profile.html')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
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
    
class WProfileList(ListView):
    model = models.WorkoutProfile
    
    def get(self, request, *args, **kwargs):
        self.user_coords = utils.get_user_coords(self.request)
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        initial = super().get_queryset().exclude(user=self.request.user).exclude(residence_location=None).annotate(location=F('residence_location'), name=Concat(F('user__first_name'), Value(' '), F('user__last_name')), description=F('user__username'))
        print(initial.query)
        user_point = Point(x=self.user_coords[1], y=self.user_coords[0], srid=4326)
        return initial.annotate(distance=Distance('residence_location', user_point)).order_by('distance')
    
    def get_context_data(self):
        ctx = super().get_context_data()
        ctx['user_loc'] = self.user_coords
        return ctx