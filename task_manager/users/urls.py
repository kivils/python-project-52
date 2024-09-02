from django.urls import path
from task_manager.users.views import (
    UsersIndexView,
    UserCreateView,
)
from . import views

urlpatterns = [
    path('<int:pk>/update/', views.update_user, name='user_update'),
    path('<int:pk>/delete/', views.delete_user, name='user_delete'),
    path('', UsersIndexView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='user_create'),
]
