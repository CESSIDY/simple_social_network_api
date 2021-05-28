from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Like


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'username', 'created_at',)

    def username(self, instance):
        try:
            name = instance.user.username
        except:
            return '-'
        return name


class LikeAdmin(admin.ModelAdmin):
    list_display = ('username', 'post_title', 'created_at',)

    def username(self, instance):
        try:
            name = instance.user.username
        except:
            return '-'
        return name

    def post_title(self, instance):
        try:
            title = instance.post.title
        except:
            return '-'
        return title


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
