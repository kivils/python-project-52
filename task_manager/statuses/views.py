from django.utils.translation import gettext_lazy as _
from .forms import StatusForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Statuses
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView


class StatusAbstractMixin:
    model = Statuses
    success_url = reverse_lazy('statuses')
    form_class = StatusForm


class StatusesIndexView(StatusAbstractMixin, ListView):
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
