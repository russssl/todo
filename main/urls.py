from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('completed/', views.CompletedTasks.as_view(), name = 'completed'),
    path('ready_js/', views.TaskEditJS.as_view(), name = 'ready'),
    path('delete_item/<int:id>', views.DeleteTask, name = 'delete_item'),
    path('delete_all/', views.DeleteAll, name = 'delete_all'),
]