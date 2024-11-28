import django_filters
from django import forms
from .models import Task
from django.contrib.auth import get_user_model


class TaskFilter(django_filters.FilterSet):
    executor = django_filters.ModelChoiceFilter(
        queryset=get_user_model().objects.all(),
        label='Исполнитель',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'users_tasks': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}),
        }