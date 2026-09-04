from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile

AppUserModel = get_user_model()

@receiver(post_save,sender=AppUserModel)
def profile_created(sender,instance,created,**kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance
        )
        profile.save()

