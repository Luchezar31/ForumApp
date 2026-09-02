from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models

from accounts.managers import CustomUserManager


class AppCustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        max_length=100,
        unique=True,
        error_messages={
            'unique':"User with that name already exist"
        }
    )

    email = models.EmailField(
        unique=True,

    )

    is_staff = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    date_joined = models.DateField(
        auto_now_add=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()