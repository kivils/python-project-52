from django.views.generic import TemplateView


class StatusesIndexView(TemplateView):
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
