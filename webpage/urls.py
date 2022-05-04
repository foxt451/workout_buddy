from django.urls import path

from webpage.views.wsess import WSessDelete, WSessUpdate
from . import views

app_name = 'webpage'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('wprofile/edit/', views.WProfileUpdate.as_view(), name='wprofile-edit'),
    path('wprofile/create/', views.WProfileCreate.as_view(), name='wprofile-create'),
    path('wsess/create/', views.WSessCreate.as_view(), name='wsess-create'),
    path('wsessions/', views.WSessList.as_view(), name='wsess-list'),
    path('wsessions/<int:pk>/', views.OwnWSessList.as_view(), name='wsess-list-own'),
    path('wbuddies/', views.WProfileList.as_view(), name='wprofile-list'),
    path('wsess/<int:pk>/', views.WSessDetail.as_view(), name='wsess-detail'),
    path('wsess-edit/<int:pk>/', views.WSessUpdate.as_view(), name='wsess-edit'),
    path('wsess-delete/<int:pk>/', views.WSessDelete.as_view(), name='wsess-delete'),
    path('wsess-delete/<int:pk>/', views.WSessDelete.as_view(), name='wsess-delete'),
    
    path('reactions/interested/', views.SayInterested.as_view(), name='say-interested'),
]