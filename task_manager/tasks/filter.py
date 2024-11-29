import django_filters
from django import forms
from .models import Task
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model


class TaskFilter(django_filters.FilterSet):
    executor = django_filters.ModelMultipleChoiceFilter(
        queryset=get_user_model().objects.all(),
        label='Исполнитель',
        required=False,
        # widget=forms.Select(attrs={'class': 'form-select'})
    )
    labels = django_filters.ModelMultipleChoiceFilter(
        queryset=Label.objects.all(),
        label='Метки',
        required=False,
        # widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
        widgets = {
            'executor': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            # 'labels': forms.SelectMultiple(attrs={'class': 'form-select'}),
            # 'users_tasks': forms.CheckboxInput(
            #     attrs={'class': 'required checkbox form-control'}),
        }
