from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone

from apps.user_profile.forms import ProfileEditForm
from apps.user_profile.models import Profile


class ProfileEditFormTests(TestCase):

    def setUp(self):
        self.user_admin = User.objects.create_user(
            username='admin',
            email='test@test.com',
            password='admin_password'
        )
        self.user_admin_profile = Profile.objects.create(
            first_name='Test',
            last_name='Tester',
            date_of_birth=datetime.today(),
            biography='some biography',
            user=self.user_admin
        )
        self.factory = RequestFactory()

    def test_edit_form(self):
        data = {
            'first_name': 'New test',
            'last_name': 'tester',
            'date_of_birth': datetime.today(),
            'biography': 'some new test',
            'user': self.user_admin,
        }
        request = self.factory.get(reverse("user_profile:index"))
        form = ProfileEditForm(data=data, request=request, instance=self.user_admin_profile)
        self.assertTrue(form.is_valid())
        self.user_admin = form.save()

        self.assertEqual(self.user_admin.first_name, 'New test')
        self.assertEqual(self.user_admin.last_name, 'tester')
        self.assertEqual(self.user_admin.biography, 'some new test')
        self.assertTrue(self.user_admin.last_edit_time < timezone.now())
        self.assertEqual(self.user_admin.last_editor_ip, '127.0.0.1')
