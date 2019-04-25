from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from .models import Request


class SaveRequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request._start_time = timezone.now()

    def process_response(self, request, response):
        request._stop_time = timezone.now()
        Request.objects.create(
            path=request.path,
            method=request.method,
            time=request._start_time,
            user=request.user,
            execution_time=request._stop_time - request._start_time,
        )
        return response
