from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm

CustomUser = get_user_model()

@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ( "email",)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login",)}),
    )

    list_display = ("username", "email", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email")