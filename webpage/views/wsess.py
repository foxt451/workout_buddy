from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from webpage import models, forms
from django.utils import timezone

class WSessCreate(LoginRequiredMixin, CreateView):
    form_class = forms.WSessForm
    model = models.WorkoutSession
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
class WSessList(ListView):
    def get_queryset(self):
        return models.WorkoutSession.objects.exclude(at__lt=timezone.now())

class WSessDetail(DetailView):
    model = models.WorkoutSession