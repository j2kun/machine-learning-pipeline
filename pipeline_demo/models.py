from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=104)
    email_age = models.IntegerField(null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    labeled_as_real = models.BooleanField(null=True)

class UserLoginEvent(models.Model):
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('User')
