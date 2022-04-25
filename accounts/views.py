from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, UpdateView
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
        
class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'phone_number', 'tz', 'username']
    
    def get_object(self):
        return get_object_or_404(self.model, id=self.request.user.id)

# from allauth.account.utils import send_email_confirmation
# class ProfileEmailUpdate(LoginRequiredMixin, UpdateView):
#     model = CustomUser
#     fields = ['email']
    
#     def get_object(self):
#         return get_object_or_404(self.model, id=self.request.user.id)
    
#     def form_valid(self, form):
#         if form.instance.email == self.request.user.email:
#             form.add_error('email', 'This is already the email you have.')
#             return self.form_invalid(form)
#         send_email_confirmation(self.request, form.instance, signup=False, email=form.instance.email)
#         return render(self.request, 'account/email_change_confirm.html')
        
# class CustomLoginView(LoginView):
#     def get_default_redirect_url(self):
#         if not hasattr(self.request.user, 'workoutprofile'):
#             # create an empty profile for the user and redirect to edit it
#             profile = WorkoutProfile(user=self.request.user)
#             profile.save()
#             return reverse('webpage:wprofile-edit')
#         else:
#             return super().get_default_redirect_url()
