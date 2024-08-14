# from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse, reverse_lazy
# from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
# , redirect
# from django.views import View
from django.views.generic import TemplateView
# from django.utils.translation import gettext_lazy as _
from task_manager.users.forms import LoginUserForm
from django.contrib.auth.views import LoginView


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('index')


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        print('fhfhfhhfhf')
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


# class TaskManagerLogoutView(View):

#     def post(self, request, *args, **kwargs):
#         logout(request)
#         messages.info(request, _('You are logged out'))
#         return redirect('index')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def page_not_found_view(request, *args, **kwargs):
    return render(request, '404.html', status=404)
