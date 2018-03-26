from __future__ import unicode_literals

import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Authentication models

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')

    # The additional attributes we wish to include.
    # The avatar property is included automatically from django-avatars
    no_reviews = models.IntegerField(default=0)
    no_likes = models.IntegerField(default=0)
    subcrawls = models.ManyToManyField('Subcrawl')

# Subcrawls
class Subcrawl(models.Model):
    sub_name = models.CharField(max_length=128, unique=True)
    sub_slug = models.SlugField(unique=True, default='')
    sub_date = models.DateField(default="2000-01-01")
    sub_time = models.TimeField(default="18:00")
    is_public = models.BooleanField(default=False)
    sub_cur_loc = models.ForeignKey('Place', null=True, on_delete=models.SET_NULL, related_name='subcrawl_loc')
    sub_places = models.ManyToManyField('Place')
    sub_organiser = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    first_st = models.ForeignKey('Station', null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.sub_slug = slugify(self.sub_name)
        super(Subcrawl, self).save(*args, **kwargs)

    def __str__(self):
        return self.sub_name

# StationPage
class Station(models.Model):
    name = models.CharField(max_length=128, unique=True,primary_key=True)
    firstTrainMonSat = models.TimeField(blank=True,null=True)
    lastTrainMonSat = models.TimeField(blank=True,null=True)
    firstTrainSun = models.TimeField(blank=True,null=True)
    lastTrainSun = models.TimeField(blank=True,null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    mapCoords = models.CharField(max_length=32,default='0,0,0,0')
    slug = models.SlugField(unique=True,default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Station, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'stations'

    def __str__(self):
        return self.name

# Places
class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128,default='')
    postcode = models.CharField(max_length=7,default='')
    address = models.CharField(max_length=128,default='')
    website = models.URLField(default='')
    closeStation = models.ForeignKey(Station,default='',on_delete=models.SET_NULL, null=True) #many-to-one mapping
    likes = models.IntegerField(default=0)

    PUB_CHOICE = 0
    RESTAURANT_CHOICE = 1
    NIGHTCLUB_CHOICE = 2
    OTHER_CHOICE = 3

    PLACE_CHOICES = (
        (PUB_CHOICE, "Pub"),
        (RESTAURANT_CHOICE, "Restaurant"),
        (NIGHTCLUB_CHOICE, "Nightclub"),
        (OTHER_CHOICE, "Other")
    )

    type = models.IntegerField(choices=PLACE_CHOICES,default=PUB_CHOICE,null=False)

    slug = models.SlugField(unique=True,default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Place, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'places'

    def __str__(self):
        return self.name


#to have multiple places, we can create an image class
class Image(models.Model):
    place = models.ForeignKey(Place,on_delete=models.SET_NULL, null=True)
    image= models.ImageField(upload_to='place_images')
    uploaded_at = models.DateTimeField(default=datetime.now, blank=True)




