from django import forms
from .models import Statuses


class StatusCreateForm(forms.ModelForm):
    name = forms.CharField(label='Имя', required=True,
                                 max_length=100,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control',
                                            'placeholder': 'Имя'}))

    class Meta:
        model = Statuses()
        fields = ['name']
