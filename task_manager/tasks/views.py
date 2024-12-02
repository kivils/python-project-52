from .models import Task
from task_manager.access_mixins import LoginRequireMixin
from .forms import TaskForm
from .filter import TaskFilter
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.views.generic import DetailView


class TaskAbstractMixin(LoginRequireMixin):
    model = Task
    login_url = "/login/"
    success_url = reverse_lazy('tasks')
    form_class = TaskForm


class TaskIndexView(FilterView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter 
    filter_set = TaskFilter


class TaskCreateView(TaskAbstractMixin, CreateView):
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request,
                         _('Tasks has been created successfully.'))
        return reverse_lazy('tasks')


class TaskUpdateView(TaskAbstractMixin, UpdateView):
    template_name = 'tasks/update.html'

    def get_success_url(self):
        messages.success(self.request,
                         _('Tasks has been updated successfully.'))
        return reverse_lazy('tasks')


class TaskDeleteView(LoginRequireMixin, DeleteView):
    model = Task
    login_url = "/login/"
    template_name = 'tasks/delete.html'

    def get_success_url(self):
        messages.success(self.request,
                         _('Tasks has been deleted successfully.'))
        return reverse_lazy('tasks')


class TaskDetailView(TaskAbstractMixin, DetailView):
    template_name = 'tasks/detail.html'