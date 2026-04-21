from django.urls import path
from .views import (
    trainee_list_api,
    trainee_detail_api,
    TraineeCreateAPI,
    TraineeUpdateAPI,
    TraineeDeleteAPI
)

urlpatterns = [
    path('', trainee_list_api, name='api-trainee-list'),
    path('details/<int:pk>/', trainee_detail_api, name='api-trainee-detail'),
    path('add/', TraineeCreateAPI.as_view(), name='api-trainee-add'),
    path('update/<int:pk>/', TraineeUpdateAPI.as_view(), name='api-trainee-update'),
    path('delete/<int:pk>/', TraineeDeleteAPI.as_view(), name='api-trainee-delete'),
]