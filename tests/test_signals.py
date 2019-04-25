from django.contrib.auth.models import User
from django.test import TestCase

from apps.core.models import LogLine


class CreateLogLineTests(TestCase):

    def test_create_logline(self):
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(LogLine.objects.count(), 0)

        self.user_admin = User.objects.create_user(
            username='admin',
            email='test@test.com',
            password='admin_password'
        )

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(LogLine.objects.count(), 1)
        self.assertEqual(LogLine.objects.first().logging_type, LogLine.CREATE)
        self.assertEqual(
            LogLine.objects.first().logging_text,
            f'New {self.user_admin._meta.app_label}.{self.user_admin._meta.model_name} "{self.user_admin}" is created!'
        )

        self.user_admin.email='new_test@test.com'
        self.user_admin.save()

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(LogLine.objects.count(), 2)
        self.assertEqual(LogLine.objects.first().logging_type, LogLine.EDIT)
        self.assertEqual(
            LogLine.objects.first().logging_text,
            f'{self.user_admin._meta.app_label}.{self.user_admin._meta.model_name} "{self.user_admin}" is edited!'
        )

        self.user_admin.delete()

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(LogLine.objects.count(), 3)
        self.assertEqual(LogLine.objects.first().logging_type, LogLine.DELETE)
        self.assertEqual(
            LogLine.objects.first().logging_text,
            f'{self.user_admin._meta.app_label}.{self.user_admin._meta.model_name} "{self.user_admin}" is deleted!'
        )
