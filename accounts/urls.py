from django.urls import path, include
from accounts.views import ProfileView, CustomLoginView


app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileView.as_view(template_name='registration/profile.html'), name='profile-self'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(template_name='registration/profile.html'), name='profile'),
    path('', include('django.contrib.auth.urls')),
]