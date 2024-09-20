from .models import Task
from django.urls import reverse_lazy
from task_manager.access_mixins import LoginRequireMixin
from .forms import TaskForm
from django.views.generic import ListView


class TaskAbstractMixin(LoginRequireMixin):
    model = Task
    login_url = "/login/"
    success_url = reverse_lazy('tasks')
    form_class = TaskForm


class TaskIndexView(TaskAbstractMixin, ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
