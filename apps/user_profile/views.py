from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .forms import ProfileEditForm
from .models import Profile


class RequestUserObjectMixin:
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        obj = queryset.get(user=self.request.user)
        return obj


class IndexView(LoginRequiredMixin, RequestUserObjectMixin, DetailView):
    model = Profile
    template_name = 'user_profile/index.html'


class EditProfileView(LoginRequiredMixin, RequestUserObjectMixin, UpdateView):
    model = Profile
    template_name = 'user_profile/edit_profile.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('user_profile:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
