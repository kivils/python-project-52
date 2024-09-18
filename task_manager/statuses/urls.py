from django.urls import path
from task_manager.statuses.views import (
    StatusesIndexView,
    StatusCreateView,
    StatusUpdateView,
)

urlpatterns = [
    # path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('', StatusesIndexView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='status_create'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
]
