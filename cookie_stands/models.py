from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class CookieStands(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name
