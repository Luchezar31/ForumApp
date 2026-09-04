from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.db.models import OneToOneField

from accounts.managers import AppUserManager


# class CustomUser(AbstractUser):
#     points = models.IntegerField(
#         blank=True,
#         null=True
#     )
#

class AppCustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        unique=True,
        max_length=150
    )

    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    date_joined = models.DateField(
        auto_now_add=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = AppUserManager()


class Profile(models.Model):

    user = OneToOneField(
        to=AppCustomUser,
        on_delete=models.CASCADE
    )

    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )


    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )









