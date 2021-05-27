from django.utils.timezone import now
from rest_framework_simplejwt.settings import api_settings
from accounts.models import User


class SetLastVisitMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response = self.process_response(request, response)
        return response

    def process_response(self, request, response):
        if request.user.is_authenticated:
            # Update last visit time after request finished processing.
            User.objects.filter(pk=request.user.pk).update(last_visit=now())
        return response
