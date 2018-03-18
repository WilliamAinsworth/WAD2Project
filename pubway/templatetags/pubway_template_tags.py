from django import template
from pubway.models import Station
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter

def get_station(inName=None):
    stations_list = Station.objects.all()

    for station in stations_list:
        if station.name == inName:
            return station
 

