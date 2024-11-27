import django_filters
from django import forms
from .models import Task
from django.contrib.auth import get_user_model
from .forms import CustomChoiceField


class TaskFilter(django_filters.FilterSet):
    # executor = CustomChoiceField(
    #     queryset=get_user_model().objects.all(),
    #     label='Исполнитель',
    #     required=False,
    #     widget=forms.Select(attrs={'class': 'form-select'})
    # )
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['name']
        # ['status', 'executor', 'labels']
        # widgets = {
        #     'status': forms.Select(attrs={'class': 'form-select'}),
        #     'labels': forms.SelectMultiple(attrs={'class': 'form-select'}),
        #     'users_tasks': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}),
        # }