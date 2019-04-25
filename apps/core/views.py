from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import LogLine, Request


class LogView(LoginRequiredMixin, ListView):
    model = LogLine
    template_name = 'core/logs.html'


class RequestView(LoginRequiredMixin, ListView):
    model = Request
    template_name = 'core/requests.html'
