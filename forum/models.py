from django.db import models
from django.db.models import ForeignKey

from forum.choices import LanguageChoices


class PostBaseModel(models.Model):
    title = models.CharField(
        max_length=100
    )

    context = models.TextField()

    author = models.CharField(
        max_length=30
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )


    language = models.CharField(
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER
    )

    image = models.ImageField(
        upload_to='media_files',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    approved = models.BooleanField(
        default=False,
    )

    class Meta:
        permissions = [
            ('can_approve_post','Can approve post base model')
        ]

class Comment(models.Model):
    post = ForeignKey(
        to=PostBaseModel,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.TextField(
        null=True,
        blank=True,

    )
    author = models.CharField(max_length=30,null=True,blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

