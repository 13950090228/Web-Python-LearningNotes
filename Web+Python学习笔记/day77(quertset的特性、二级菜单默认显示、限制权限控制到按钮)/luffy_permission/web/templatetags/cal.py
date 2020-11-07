


from django.utils.safestring import mark_safe

from django.template import Library
register =Library()


@register.filter
def mul(x,y):
    return x*y

@register.filter
def tag(val):
    return mark_safe("<a>%s</a>"%val)

@register.filter
def lower(val):

    return val.lower()

@register.simple_tag
def mul_tag(x,y,z):
    return x*y*z



@register.inclusion_tag("web/menu.html")
def get_menu_style():
    menu_list=[123,666,999]
    return {"menu_list":menu_list}



