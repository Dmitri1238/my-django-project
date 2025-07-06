from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # главная страница
    path('posts/<int:id>/', views.post_detail, name='post_detail'),  # детали поста
]