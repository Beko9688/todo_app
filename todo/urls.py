from django.contrib import admin
from django.urls import path
from todoapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('update_task/<str:pk>', updateTask, name='update_task'),
    path('delete_task/<str:pk>', deleteTask, name='delete_task'),
    path('strike_task/<str:pk>', strikeTask, name='strike_task'),
    path('delete_all', delete_all, name='delete_all'),
]
