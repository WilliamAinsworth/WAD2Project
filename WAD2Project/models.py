from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


#Authentication system

class User(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    forename = models.TextField()
    surname = models.TextField()
    nickname = models.TextField()
    email = models.EmailField()
    no_reviews = models.IntegerField()
    no_likes = models.IntegerField()
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # if Python 2.7.x
    def __str__(self):
        return self.user.nickname