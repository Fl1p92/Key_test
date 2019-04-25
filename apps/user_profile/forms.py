from datetime import datetime

from django import forms

from .models import Profile


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'date_of_birth', 'biography', 'contacts',)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        object = super().save(commit=False)
        object.last_edit_time = datetime.now()
        object.last_editor_ip = self.get_client_ip()
        object.save()
        self.save_m2m()
        return object

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip
