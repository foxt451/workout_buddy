from django.urls import path, include
from accounts.views import ProfileView


app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileView.as_view(template_name='registration/profile.html'), name='profile-self'),
    path('profile/<int:pk>/', ProfileView.as_view(template_name='registration/profile.html'), name='profile'),
    path('', include('django.contrib.auth.urls')),
]