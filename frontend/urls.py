from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),  # Assuming home view is a list view
    path('tasks/', TaskListView.as_view(), name='task_list'),  # List all tasks
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),  # Create new task
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),  # Update a specific task
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),  # Detail view for a specific task
    # Add more routes as needed
]
