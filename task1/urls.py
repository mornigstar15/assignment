from django.urls import path
from .views import SignUpView, TasksView,TasksListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('tasks/', TasksListView.as_view(), name='tasks'),
    path('tasks/create', TasksView.as_view(), name='create_task'),
]
