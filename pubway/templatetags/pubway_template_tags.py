from django import template
from pubway.models import Place

register = template.Library()

@register.inclusion_tag('pubway/plcs.html')
def get_close_places_list(stn=None):
   return {'plcs': Place.objects.filter(closeStation=stn)}
#To get places closest to given station use: {% get_close_places_list 'Hillhead' %}