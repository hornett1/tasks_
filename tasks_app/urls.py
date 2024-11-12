from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('<int:pk>/', DetailTask.as_view(), name="detail-task"),
    path('profile/', TaskListViewProfile.as_view(), name="task-status"),
    path('update_status/<int:task_id>/', update_task_status, name='update-task-status'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('delete/<int:pk>/', DeleteTaskView.as_view(), name='delete-task'),
]