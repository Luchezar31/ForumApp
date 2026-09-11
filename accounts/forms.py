from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm


CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email')
        
