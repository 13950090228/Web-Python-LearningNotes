from django import template

register = template.Library()

from django.conf import settings
import re


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_list = request.session.get(settings.MENU_SESSION_KEY)
    
    return {"menu_list": menu_list}
