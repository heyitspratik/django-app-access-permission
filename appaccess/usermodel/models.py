from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True, null=True, unique=True, default=None)
    mobile_number = models.CharField(_('Mobile Number'), max_length=20, blank=True, null=True, unique=True)
    email_verified = models.BooleanField(default=True)
    dob = models.DateField(blank=True, null=True)
