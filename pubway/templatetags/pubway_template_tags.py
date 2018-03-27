from django import template
from pubway.models import Place

register = template.Library()

@register.inclusion_tag('pubway/plcs.html')
def get_close_places_list(stn=None):
   return {'plcs': Place.objects.filter(closeStation=stn)}
#To get places closest to given station use: {% get_close_places_list 'Hillhead' %}

@register.inclusion_tag('pubway/top_plcs.html')
def get_top_places_list(stn=None):
    stationPlaces = Place.objects.filter(closeStation=stn)
    top_places = stationPlaces.order_by('-likes')[:5]

    return { 'top_plcs' : top_places }

@register.filter(name='getType')
def getType(value):
    for element in Place.PLACE_CHOICES:
        if value in element:
            return element[1]
    return "Type not found"