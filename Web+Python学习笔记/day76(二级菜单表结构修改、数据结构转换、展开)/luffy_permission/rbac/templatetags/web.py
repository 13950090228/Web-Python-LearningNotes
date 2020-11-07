

from django.utils.safestring import mark_safe
from django.template import Library
import re
register =Library()


@register.inclusion_tag("rbac/menu.html")
def get_menu_styles(request):
    permission_menu_dict = request.session.get("permission_menu_dict")
    print("permission_menu_dict",permission_menu_dict)
    return {"permission_menu_dict":permission_menu_dict}




