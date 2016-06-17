from django import template
from reservation.models import Instrument

register = template.Library()

@register.inclusion_tag('reservation/instruments.html')
def get_instrument_list():
    return {'instruments': Instrument.objects.all()}
