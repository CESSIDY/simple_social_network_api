from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(CustomUserAdmin, self).__init__(*args, **kwargs)

    list_display = ('username', 'email', 'last_visit', 'last_login', 'is_staff')


admin.site.register(User, CustomUserAdmin)
