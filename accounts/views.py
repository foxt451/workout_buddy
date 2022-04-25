from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from django.contrib.auth.views import LoginView
from webpage.models import WorkoutProfile

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    
    def get_object(self, queryset=CustomUser):
        if 'pk' in self.kwargs:
            return get_object_or_404(queryset, id=self.kwargs['pk'])
        else:
            return get_object_or_404(queryset, id=self.request.user.id)
        
# class CustomLoginView(LoginView):
#     def get_default_redirect_url(self):
#         if not hasattr(self.request.user, 'workoutprofile'):
#             # create an empty profile for the user and redirect to edit it
#             profile = WorkoutProfile(user=self.request.user)
#             profile.save()
#             return reverse('webpage:wprofile-edit')
#         else:
#             return super().get_default_redirect_url()
