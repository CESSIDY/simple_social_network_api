from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    last_visit = models.DateTimeField(verbose_name='Last visit', blank=True, null=True)
    last_login = models.DateTimeField(verbose_name='Last login', blank=True, null=True)

    def update_last_login(self):
        self.last_login = now()
        self.save()
