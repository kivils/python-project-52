from django import forms
from .models import Task
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model


class TaskForm(forms.ModelForm):
    name = forms.CharField(label='Имя', required=True,
                                 max_length=100,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control',
                                            'placeholder': 'Имя'}))

    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control',
                                             'placeholder': 'Описание',
                                             "rows": 10, "cols": 20}))

    STATUSES = ((name, name) for name in
                Statuses.objects.values_list("name", flat=True))

    status = forms.ChoiceField(label='Статус', required=True,
                               choices=STATUSES,
                               widget=forms.Select(
                                attrs={'class': 'form-select'}))

    EXECUTORS = ((username, username) for username in
                 get_user_model().objects.values_list("username", flat=True))

    executor = forms.ChoiceField(label='Исполнитель',
                                 choices=EXECUTORS,
                                 widget=forms.Select(
                                        attrs={'class': 'form-select'}))

    LABELS = ((name, name) for name in
              Label.objects.values_list("name", flat=True))

    labels = forms.ChoiceField(label='Метки',
                               choices=LABELS,
                               widget=forms.Select(
                                     attrs={'class': 'form-select',
                                            'multiple': True}))

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
