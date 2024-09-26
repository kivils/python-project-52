from django import forms
from .models import Task


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

    status = forms.CharField(label='Статус', required=True,
                             widget=forms.Select(
                                attrs={'class': 'form-select',
                                       'autocomplete': 'on'}))

    executor = forms.CharField(label='Исполнитель',
                                     widget=forms.Select(
                                        attrs={'class': 'form-select',
                                               'autocomplete': 'on'}))

    labels = forms.CharField(label='Метки',
                                   widget=forms.Select(
                                     attrs={'class': 'form-select',
                                            'multiple': True}))

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
