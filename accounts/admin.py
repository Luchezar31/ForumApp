from django.contrib import admin

from accounts.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass
