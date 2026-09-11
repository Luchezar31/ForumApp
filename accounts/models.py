<<<<<<< HEAD
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
=======
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
>>>>>>> 3e503cac61284b7e60aa02e3e329fdd2b1da61fe
from django.db import models
from django.db.models import OneToOneField

from accounts.managers import AppUserManager

from accounts.managers import CustomUserManager

<<<<<<< HEAD
=======
# class CustomUser(AbstractUser):
#     points = models.IntegerField(
#         blank=True,
#         null=True
#     )
#
>>>>>>> 3e503cac61284b7e60aa02e3e329fdd2b1da61fe

class AppCustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
<<<<<<< HEAD
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
=======
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









>>>>>>> 3e503cac61284b7e60aa02e3e329fdd2b1da61fe
