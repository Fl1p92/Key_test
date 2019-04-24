from django.views.generic import DetailView

from .models import Profile


class IndexView(DetailView):
    model = Profile
    template_name = 'user_profile/index.html'
