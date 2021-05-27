from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('api/create/', CreatePostView.as_view(), name='post_create'),
    path('api/like/<int:pk>/', LikePostView.as_view(), name='post_like'),
    path('api/unlike/<int:pk>/', UnLikePostView.as_view(), name='post_unlike'),
]
