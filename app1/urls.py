from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # главная страница с списком постов
    path('add/', views.add_post, name='add_post'),  # страница добавления поста
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),  # удаление поста
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)