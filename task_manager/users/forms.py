# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import BaseUserCreationForm
from django import forms


class UserCreateForm(forms.Form):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
                                     attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input'}))


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
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
