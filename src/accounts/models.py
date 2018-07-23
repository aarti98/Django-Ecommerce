from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
)


class User(AbstractBaseUser):
    pass


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email