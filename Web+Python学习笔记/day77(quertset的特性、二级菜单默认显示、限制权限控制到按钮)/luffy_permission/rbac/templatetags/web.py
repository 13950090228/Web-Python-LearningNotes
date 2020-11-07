

from django.utils.safestring import mark_safe
from django.template import Library
import re
register =Library()


@register.inclusion_tag("rbac/menu.html")
def get_menu_styles(request):
    permission_menu_dict = request.session.get("permission_menu_dict")
    print("permission_menu_dict",permission_menu_dict)

    for val in permission_menu_dict.values():
        for item in val["children"]:
            val["class"]="hide"

            ret=re.search("^{}$".format(item["url"]),request.path)
            if ret:
                val["class"] = ""

    return {"permission_menu_dict":permission_menu_dict}






@register.filter
def has_permission(btn_url,request):
    permission_names = request.session.get("permission_names")

    return btn_url in permission_names









'''

{
       1:{
            "title":"信息管理",
            "icon":"",
            "children":[
                {
                  "title":"客户列表",
                  "url":"",
                }
            ]
            
          },
          
       2:{
            "title":"财务管理",
            "icon":"",
            "children":[
                {
                  "title":"缴费列表",
                  "url":"",
                },
            ]
            
          }, 
      
    
    }
    



'''


