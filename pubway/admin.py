from django.contrib import admin
from pubway.models import UserProfile
from pubway.models import Station, Place, Subcrawl

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Station)
admin.site.register(Place)
admin.site.register(Subcrawl)
