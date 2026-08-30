from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email')
        
