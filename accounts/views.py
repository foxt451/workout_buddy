from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    
    def get_object(self, queryset):
        if 'pk' in self.kwargs:
            return get_object_or_404(queryset, id=self.kwargs['pk'])
        else:
            return get_object_or_404(queryset, id=self.request.user.id)
