from django.contrib import admin

from forum.models import PostBaseModel


@admin.register(PostBaseModel)
class PostAdmin(admin.ModelAdmin):
    pass
