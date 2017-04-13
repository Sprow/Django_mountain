from django import template
from datetime import datetime

register = template.Library()

@register.filter(is_safe=True)
def our_castom_datetime(value) :
    # now = datetime.now()
    # if value.year == now.year and value.month == now.month and
    return value.strftime("%m-%d-%Y")
