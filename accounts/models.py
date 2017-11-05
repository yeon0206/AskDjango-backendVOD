#accounts/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # user = models.OneToOneField(User) # BAD CASE! 다른유저모델을 쓸수 있기때문에
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)