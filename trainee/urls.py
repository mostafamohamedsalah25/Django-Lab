from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainee_list, name='trainee_list'),
    path('details/<int:id>/', views.trainee_detail, name='trainee_detail'),
    path('add/', views.TraineeCreateView.as_view(), name='add_trainee'),
    path('update/<int:pk>/', views.TraineeUpdateView.as_view(), name='update_trainee'),
    path('delete/<int:pk>/', views.TraineeDelete.as_view(), name='delete_trainee'),
]
