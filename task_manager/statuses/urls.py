from django.urls import path
from task_manager.statuses.views import (
    StatusesIndexView,
)

urlpatterns = [
    # path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    # path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('', StatusesIndexView.as_view(), name='statuses'),
    # path('create/', UserCreateView.as_view(), name='user_create'),
]
