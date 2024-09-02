from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from task_manager.users.forms import UserCreateForm
# , UserDeleteForm
from task_manager.view_mixins import IndexViewMixin
# , CreateViewMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.contrib import messages
# from django.contrib.auth import logout
from django.contrib.auth.models import User


class UsersAbstractMixin:
    model = get_user_model()
    success_url = reverse_lazy('users')
    form_class = UserCreateForm


class UsersIndexView(UsersAbstractMixin, IndexViewMixin):
    template_name = 'users/index.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'

    def get_success_url(self):
        messages.success(self.request,
                         _('User has been registered successfully.'))
        return reverse_lazy('login')


class UserUpdateView():
    success_url = reverse_lazy('index')
    template_name = 'users/update.html'


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    login_url = '/login/'
    template_name = 'users/delete.html'

    def get(self, request, pk):
        if pk != self.request.user.id:
            messages.error(request,
                           _('You do not have permission to'
                             ' change another user.'))
            return HttpResponseRedirect(reverse('users'))
        else:
            return render(request, 'users/delete.html')

    # не работает, это исправить
    def get_success_url(self):
        # messages.success(self.request,
        #                  _('User has been deleted successfully.'))
        return HttpResponseRedirect(reverse('index'))


def update_user(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(request,
                             _('User has been updated successfully.'))
            return HttpResponseRedirect(reverse('index',
                                                kwargs={'pk': new_user.id}))
    else:
        if not request.user.is_authenticated:
            messages.error(request,
                           _('You are not authorized please login.'))
            return HttpResponseRedirect(reverse('login'))
        else:
            if request.user.id != pk:
                messages.error(request,
                               _('You do not have permission to'
                                 ' change another user.'))
                return HttpResponseRedirect(reverse('users'))
            else:
                form = UserCreateForm(instance=user)
    return render(request, 'users/update.html', {'form': form})


# def delete_user(request, pk):
#     if request.method == 'POST':
#         form = UserDeleteForm(request.POST)
#         if form.is_valid():
#             user = request.user
#             logout(request)
#             user.delete()
#             messages.success(request,
#                              _('User has been deleted successfully.'))
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         if not request.user.is_authenticated:
#             messages.error(request,
#                            _('You are not authorized please login.'))
#             return HttpResponseRedirect(reverse('login'))
#         else:
#             if request.user.id != pk:
#                 messages.error(request,
#                                _('You do not have permission to'
#                                  ' change another user.'))
#                 return HttpResponseRedirect(reverse('users'))
#             else:
#                 form = UserDeleteForm()
#     return render(request, 'users/delete.html', {'form': form})
