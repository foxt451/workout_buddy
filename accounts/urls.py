from django.urls import path, include
from accounts.views import ProfileView, ProfileUpdate#, ProfileEmailUpdate


app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileView.as_view(template_name='registration/profile.html'), name='profile-self'),
    #path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(template_name='registration/profile.html'), name='profile'),
    path('profile/edit/', ProfileUpdate.as_view(template_name='registration/profile_form.html'), name='profile-edit'),
    #path('profile/email/edit/', ProfileEmailUpdate.as_view(template_name='registration/profile_form.html'), name='profile-email-edit')
    #path('', include('allauth.urls')),
    #path('', include('django.contrib.auth.urls')),
]