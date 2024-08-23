from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from task_manager.users.forms import UserCreateForm, UserDeleteForm
from task_manager.view_mixins import IndexViewMixin
from django.contrib import messages
from django.contrib.auth import logout


class UsersAbstractMixin:
    model = get_user_model()
    success_url = reverse_lazy('users')
    form_class = UserCreateForm


class UsersIndexView(UsersAbstractMixin, IndexViewMixin):
    template_name = 'users/index.html'
    context_object_name = 'users'


class UserCreateView():
    success_url = reverse_lazy('login')
    template_name = 'users/create.html'
    success_message = _('User has been registered successfully.')


class UserUpdateView():
    success_url = reverse_lazy('index')
    template_name = 'users/update.html'
    success_message = _('User has been updated successfully.')


class UserDeleteView():
    success_url = reverse_lazy('delete')
    template_name = 'users/delete.html'
    success_message = _('User has been deleted successfully.')


def register_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreateForm()
    return render(request, 'users/create.html', {'form': form})


def update_user(request, pk):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return HttpResponseRedirect(reverse('index',
                                                kwargs={'pk':   new_user.id}))
    else:
        # # if request == User.objects.get(id=user_id):
        # user = User.objects.get(id=pk)
        # print(user, 'userrr')
        # if request == user:
        form = UserCreateForm()
    return render(request, 'users/update.html', {'form': form})


def delete_user(request, pk):
    if request.method == 'POST':
        form = UserDeleteForm(request.POST)
        print(form.is_valid(), 'fijfiejfijfifjifj')
        if form.is_valid():
            user = request.user
            logout(request)
            user.delete()
            messages.success(request, 'Account successfully deleted')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserDeleteForm()
    return render(request, 'users/delete.html', {'form': form})
