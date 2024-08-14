from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import BaseUserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    # first_name = forms.CharField(label='Имя', widget=forms.TextInput(
    #                                  attrs={'class': 'form-input'}))
    # last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
    #     attrs={'class': 'form-input'}))
    # username = forms.CharField(label='Имя пользователя',
    #                            widget=forms.TextInput(
    #                                attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
# class UserCreateForm(BaseUserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'password1',
#             'password2'
#         ]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields[
#             self._meta.model.USERNAME_FIELD].widget.attrs.pop('autofocus')
