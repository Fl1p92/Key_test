from django.views.generic import ListView

from .models import LogLine, Request


class LogView(ListView):
    model = LogLine
    template_name = 'core/logs.html'


class RequestView(ListView):
    model = Request
    template_name = 'core/requests.html'
