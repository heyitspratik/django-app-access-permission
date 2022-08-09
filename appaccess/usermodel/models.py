from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=20, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), blank=True, null=True, unique=True, default=None)
    email_verified = models.BooleanField(default=True)
    dob = models.DateField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        if self.email:
            return self.email
        return str(self.pk)
