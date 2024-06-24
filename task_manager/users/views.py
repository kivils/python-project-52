# from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class UsersIndexView(TemplateView):
    template_name = 'users/index.html'
    context_object_name = 'users'
