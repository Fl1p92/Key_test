from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from .models import Profile


class IndexView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'user_profile/index.html'
