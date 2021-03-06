from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from webpage import models, forms
from django.utils import timezone
from django.urls import reverse
from django.contrib.gis.geos import Point
from django.db.models import Q
from django.contrib.gis.forms.widgets import OSMWidget
from . import utils
from django.contrib.gis.db.models.functions import Distance


class WSessCreate(LoginRequiredMixin, CreateView):
    form_class = forms.WSessForm
    model = models.WorkoutSession

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        coords = utils.get_user_coords(self.request)
        ctx = super().get_context_data(**kwargs)
        ctx['y'], ctx['x'] = coords
        return ctx

    # def get_form(self):
    #     form = super().get_form()
    #     # utils.set_form_field_widget_to_leaflet_with_default_location(
    #     #     self.request, form, 'location')
    #     # utils.set_form_field_widget_to_google_with_default_location(
    #     #     self.request, form, 'location')
    #     return form
    
class WSessUpdate(LoginRequiredMixin, UpdateView):
    form_class = forms.WSessForm
    model = models.WorkoutSession
    
    # better than test_func, since in test_func we would have to use get_object() making a database hit twice a view, this way - one
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(creator=self.request.user)
        return queryset
    
class WSessDelete(LoginRequiredMixin, DeleteView):
    model = models.WorkoutSession
    
    def get_success_url(self):
        return reverse('webpage:wsess-list')
    
    # better than test_func, since in test_func we would have to use get_object() making a database hit twice a view, this way - one
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'webpage.delete_workoutsession' in self.request.user.get_all_permissions():
            return queryset
        queryset = queryset.filter(creator=self.request.user)
        return queryset


class WSessList(ListView):
    model = models.WorkoutSession
    
    def get_queryset(self):
        exclude_outdated = super().get_queryset().exclude(at__lt=timezone.now())
        user_coords = utils.get_user_coords(self.request)
        user_point = Point(x=user_coords[1], y=user_coords[0], srid=4326)
        return exclude_outdated.annotate(distance=Distance('location', user_point)).order_by('distance')
    
    def get_context_data(self):
        ctx = super().get_context_data()
        coords = utils.get_user_coords(self.request)
        ctx['user_loc'] = coords
        return ctx
    
class OwnWSessList(ListView):
    model = models.WorkoutSession
    
    def get_queryset(self):
        initial = super().get_queryset().filter(creator__id=self.kwargs['pk'])
        user_coords = utils.get_user_coords(self.request)
        user_point = Point(x=user_coords[1], y=user_coords[0], srid=4326)
        return initial.annotate(distance=Distance('location', user_point)).order_by('distance')
    
    def get_context_data(self):
        ctx = super().get_context_data()
        coords = utils.get_user_coords(self.request)
        ctx['user_loc'] = coords
        return ctx


class WSessDetail(DetailView):
    model = models.WorkoutSession

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['loc_widget'] = OSMWidget(attrs={'geom_type': 'POINT'})
    #     return context
