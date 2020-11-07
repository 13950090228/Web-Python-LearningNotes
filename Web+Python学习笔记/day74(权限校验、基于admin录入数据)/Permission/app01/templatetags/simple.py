from django.template import Library
from django.utils.safestring import mark_safe
register = Library()

@register.filter
def tag(val):
    return mark_safe("<a href=#>%s</a>"%(val))

@register.filter
def lower(val):
    return val.lower()


@register.filter
def mul(x,y):
    return x*y

@register.simple_tag
def add(x,y,z):
    return x+y+z