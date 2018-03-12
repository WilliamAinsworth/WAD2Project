from __future__ import unicode_literals

import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Authentication models

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    no_reviews = models.IntegerField(default=0)
    no_likes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    subcrawls = models.ManyToManyField('Subcrawl')

# Subcrawls
class Subcrawl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, unique=False) # Unique? Pros: nice url; cons: long names required after a while
    date_time = models.DateTimeField()
    is_public = models.BooleanField()
    loc = models.ForeignKey('Place', null=True, on_delete=models.SET_NULL, related_name='subcrawl_loc')
    places = models.ManyToManyField('Place')
    organiser = models.ForeignKey('UserProfile', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# StationPage
class Station(models.Model):
    name = models.CharField(max_length=128, unique=True)
    stringName = models.CharField(max_length=128,default='')
    firstTrainMonSat = models.TimeField(blank=True,null=True)
    lastTrainMonSat = models.TimeField(blank=True,null=True)
    firstTrainSun = models.TimeField(blank=True,null=True)
    lastTrainSun = models.TimeField(blank=True,null=True)

    slug = models.SlugField(unique=True,default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Station, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# Places
class Place(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    closeStation = models.ForeignKey(Station,default='') #many-to-one mapping
    name = models.CharField(max_length=128,default='')
    postcode = models.CharField(max_length=7,default='')
    address = models.CharField(max_length=128,default='')
    website = models.URLField(default='')
    relevance = forms.ChoiceField(label="",widget=forms.Select(),required=True)


