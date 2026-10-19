from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import send_mail

from forum.models import PostBaseModel



def _send_email_on_approve(subject,message,from_email,recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list
    )



@receiver(signal=post_save,sender=PostBaseModel)
def send_email_on_approve(sender,instance,created,**kwargs):
    if not created and instance.approved:
        _send_email_on_approve(
            subject="Appoved post",
            message='Your post was approved',
            from_email='noreply@forum.app',
            recipient_list=[instance.user.email],
        )