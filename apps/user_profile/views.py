from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .forms import ProfileEditForm


class RequestUserProfileMixin:
    def get_object(self, queryset=None):
        profile = None
        if hasattr(self.request.user, 'profile'):
            profile = self.request.user.profile
        return profile


class IndexView(LoginRequiredMixin, RequestUserProfileMixin, DetailView):
    template_name = 'user_profile/index.html'


class EditProfileView(LoginRequiredMixin, RequestUserProfileMixin, UpdateView):
    template_name = 'user_profile/edit_profile.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('user_profile:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
