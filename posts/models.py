from django.db import models
from accounts.models import User
from django.utils.timezone import now


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="posts")
    title = models.CharField(verbose_name='Title', max_length=200)
    body = models.TextField(verbose_name='Body')
    created_at = models.DateTimeField(default=now)

    def like(self, user):
        like, is_created = Like.objects.get_or_create(post=self,
                                                      user=user)
        return like

    # remove like to article(obj)
    def unlike(self, user):
        Like.objects.filter(post=self,
                            user=user
                            ).delete()

    # check if the user liked article(obj)
    def is_fan(self, user) -> bool:
        likes = Like.objects.filter(post=self,
                                    user=user)
        return likes.exists()

    # get all users who liked articles
    def get_fans(self):
        return User.objects.filter(post=self)


class Like(models.Model):
    user = models.ForeignKey(User,
                             related_name='likes',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)
