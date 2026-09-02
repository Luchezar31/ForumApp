
from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):

    def create_user(self, email, username = None, password = None, **kwargs):

        return super().create_user(email, username, password, **kwargs)

    def create_superuser(self, email, username=None, password=None, **kwargs):

        return super().create_superuser(email, username, password, **kwargs)

    