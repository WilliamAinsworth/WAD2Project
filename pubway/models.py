from __future__ import unicode_literals

import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


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

# Places
class Place(models.Model):
    pass # Matt: needed this for  foreign key

# Something else...