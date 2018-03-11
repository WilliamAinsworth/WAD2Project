from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from pubway.models import UserProfile

#User Management

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

class UserEditForm(UserChangeForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'picture',)
