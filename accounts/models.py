#accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User) # BAD CASE!
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)