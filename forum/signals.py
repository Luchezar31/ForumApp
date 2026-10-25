from django.db.models.signals import post_save
from django.dispatch import receiver

from forum.models import PostBaseModel
from forum.tasks import _send_email_on_approve

@receiver(signal=post_save,sender=PostBaseModel)
def send_email_on_approve(sender,instance,created,**kwargs):
    if not created and instance.approved:
        _send_email_on_approve.delay(
            subject="Approved post",
            message='Your post was approved',
            from_email='noreply@forum.app',
            recipient_list=[instance.author.email],
        )


