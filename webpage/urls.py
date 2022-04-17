from django.urls import path
from . import views

app_name = 'webpage'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('wprofile-edit/', views.WProfileUpdate.as_view(), name='wprofile-edit'),
    path('wsess-create/', views.WSessCreate.as_view(), name='wsess-create'),
    path('wsessions/', views.WSessList.as_view(), name='wsess-list'),
    path('wsess/<int:pk>/', views.WSessDetail.as_view(), name='wsess-detail')
]