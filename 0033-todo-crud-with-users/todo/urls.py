from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('new/', views.new_task, name='new_task'),
    path('task/<int:pk>/completed', views.completed_task, name='completed_task'),
    path('task/<int:pk>/edit', views.edit_task, name='edit_task'),
    path('task/<int:pk>/delete', views.delete_task, name='delete_task')
]
