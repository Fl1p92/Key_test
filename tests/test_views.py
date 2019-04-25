from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.shortcuts import reverse
from django.template.loader import render_to_string

from apps.user_profile.models import Profile


class ProfileViewTests(TestCase):

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

    def test_index_view(self):
        self.client.login(username='admin', password='admin_password')
        path = reverse('user_profile:index')
        response = self.client.get(path)
        request = {'path': path}
        rendered_page = render_to_string(
            'user_profile/index.html',
            {'profile': Profile.objects.first(), 'user': self.user_admin, 'request': request}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_profile/index.html")
        self.assertContains(response, render_to_string("footer.html"))
        self.assertEqual(response.content.decode("utf-8"), rendered_page)

    def test_non_auth_request(self):
        response = self.client.get(reverse('user_profile:index'))
        self.assertEqual(response.status_code, 302)
