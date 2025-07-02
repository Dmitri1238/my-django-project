from django.urls import path
from . import views

urlpatterns = [
    path('workers/', views.worker_list, name='worker_list'),
    path('workers/<int:pk>/', views.worker_detail, name='worker_detail'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
]