from django.urls import path
from task_manager.tasks.views import (
    TaskIndexView,
)

urlpatterns = [
    path('', TaskIndexView.as_view(), name='tasks'),
]
