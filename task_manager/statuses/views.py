from django.utils.translation import gettext_lazy as _
from .forms import StatusForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Statuses
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.access_mixins import LoginRequireMixin
from django.views.generic import ListView


class StatusAbstractMixin(LoginRequireMixin):
    model = Statuses
    login_url = "/login/"
    success_url = reverse_lazy('statuses')
    form_class = StatusForm


class StatusIndexView(StatusAbstractMixin, ListView):
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'


class StatusCreateView(StatusAbstractMixin, CreateView):
    template_name = 'statuses/create.html'

    def get_success_url(self):
        messages.success(self.request,
                         _('Status has been created successfully.'))
        return reverse_lazy('statuses')


class StatusUpdateView(StatusAbstractMixin, UpdateView):
    template_name = 'statuses/update.html'

    def get_success_url(self):
        messages.success(self.request,
                         _('Status has been updated successfully.'))
        return reverse_lazy('statuses')


class StatusDeleteView(LoginRequireMixin, DeleteView):
    model = Statuses
    login_url = "/login/"
    template_name = 'statuses/delete.html'
    failure_message = _('Cannot delete status because it is in use.')

    def get_success_url(self):
        messages.success(self.request,
                         _('Status has been deleted successfully.'))
        return reverse_lazy('statuses')
