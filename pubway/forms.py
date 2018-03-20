from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from pilkit.processors import ResizeToFill

from pubway.models import Place
from pubway.models import UserProfile
from imagekit.forms import ProcessedImageField

from pubway.models import Subcrawl


# User Management

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(RegistrationForm, self).save(commit=True)
        # UserProfile creation
        userprofile = UserProfile(user=user)
        userprofile.save()
        return user


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)


class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name of the place (required):", required=True)

    class Meta:
        model = Place
        exclude = ()


class SubcrawlForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                            help_text="Please enter the title of the subcrawl.")
    is_public = forms.BooleanField()
    places = forms.MultiValueField()

    class Meta:
        model = Subcrawl
        exclude = ('id','loc','organiser')
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'})
        }
