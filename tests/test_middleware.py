from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.shortcuts import reverse

from apps.core.models import Request
from apps.core.middleware import SaveRequestMiddleware
from apps.user_profile.views import IndexView


class SaveRequestMiddlewareTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user_admin = User.objects.create_user(
            username='admin',
            email='test@test.com',
            password='admin_password'
        )

    def test_save_request_middleware(self):
        self.assertEqual(Request.objects.count(), 0)

        request = self.factory.get(reverse("user_profile:index"))
        request.user = self.user_admin
        middleware = SaveRequestMiddleware(get_response=IndexView.as_view())
        response = middleware(request)
        request_object = Request.objects.first()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Request.objects.count(), 1)
        self.assertEqual(str(request.user), request_object.user)
        self.assertEqual(request.path, request_object.path)
        self.assertEqual(request.method, request_object.method)
        self.assertEqual(request._start_time, request_object.time)
        self.assertEqual(
            request._stop_time - request._start_time,
            request_object.execution_time
        )
