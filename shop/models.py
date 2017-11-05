from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    # # blog/models.py
    # class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_post_set')
    # # shop/models.py
    # class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shop_post_set') 
     # +: user.post_set.all() 사용을 포기하겠다.
     # shop.models.Post.objects.filter(user=user)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upadated_at = models.DateTimeField(auto_now=True)