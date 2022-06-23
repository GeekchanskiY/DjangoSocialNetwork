from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DMTUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = DMTUser
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = DMTUser
        fields = ('email', 'username')
