from django.contrib import admin
from django.urls import path, register_converter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *
from django.urls import path, include
from datetime import datetime


class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value


register_converter(DateConverter, 'yyyy')

app_name = 'accounts'

urlpatterns = [
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/likes/count/date_from=<yyyy:date_from>/date_to=<yyyy:date_to>/',
         LikesCountView.as_view(),
         name='likes_count'),
]
