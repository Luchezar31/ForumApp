from django.contrib import admin
from django.contrib.auth import get_user_model


AppUser = get_user_model()

@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    pass
