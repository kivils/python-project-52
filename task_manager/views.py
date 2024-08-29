from django.contrib.auth import logout, login, authenticate
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from task_manager.users.forms import LoginUserForm
# , LogoutUserForm
from django.contrib.auth.views import LoginView
# , LogoutView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUser(LoginView):
    success_url = reverse_lazy('index')
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        messages.success(self.request, _('You are logged in'))
        return reverse_lazy('index')


# class LogoutUser(LogoutUser):


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.info(request, _('You are logged out'))
    return HttpResponseRedirect(reverse('login'))


def page_not_found_view(request, *args, **kwargs):
    return render(request, '404.html', status=404)
