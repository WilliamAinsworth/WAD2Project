from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from bootstrap3_datetime.widgets import DateTimePicker

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
    name = forms.CharField(max_length=128, required=True, help_text= "Name (required)")
    postcode = forms.CharField(max_length=7,help_text= "Postcode (required)")
    address = forms.CharField(max_length=128, help_text= "Address (required)")
    url = forms.URLField(help_text="Website URL",required=False)
    type = forms.ChoiceField(choices=Place.PLACE_CHOICES, initial=Place.PUB_CHOICE)

    class Meta:
        model = Place
        exclude = ('id','closeStation','likes','slug',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('website')

        if url and not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data

class SubcrawlForm(forms.ModelForm):
    sub_name = forms.CharField(max_length=128,
                               help_text="Please enter the title of the subcrawl.")
    sub_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    sub_time = forms.TimeField()#widget=DateTimePicker()
    is_public = forms.BooleanField(initial=True)
    first_st = forms.ModelChoiceField(queryset=Station.objects.all())

    class Meta:
        model = Subcrawl
        fields = ('sub_name', 'sub_date', 'is_public','sub_time', 'first_st',)
