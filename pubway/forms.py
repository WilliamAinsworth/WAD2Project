from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from pubway.models import Place
from pubway.models import UserProfile

from pubway.models import Subcrawl, Station
from WAD2Project import settings


# User Management

# Registration form to be used to create a new User
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(RegistrationForm, self).save(commit=True)
        # UserProfile creation from User model
        userprofile = UserProfile(user=user)
        userprofile.save()
        return user

# Profile form that allows users to edit their details
class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)

# Subcrawl Management

class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=128, required=True, )
    postcode = forms.CharField(max_length=7)
    address = forms.CharField(max_length=128)
    website = forms.URLField()
    type = forms.ChoiceField(choices=Place.PLACE_CHOICES, initial=Place.PUB_CHOICE)

    class Meta:
        model = Place
        exclude = ('id','closeStation','likes','slug',)

class SubcrawlForm(forms.ModelForm):
    sub_name = forms.CharField(max_length=128,
                            help_text="Please enter the title of the subcrawl.")
    sub_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    sub_time = forms.TimeField(widget=forms.TimeInput(attrs={'class':'timepicker'}))
    is_public = forms.BooleanField(initial=True)
    first_st = forms.ModelChoiceField(queryset=Station.objects.all())
    #sub_places = forms.MultiValueField()

    class Meta:
        model = Subcrawl
        fields = ('sub_name', 'sub_date', 'is_public','sub_time', 'first_st')
