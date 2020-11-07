1 url控制器

urls.py
(1) 简单使用：通过正则分组获取url中的动态参数
(2) 有名分组：给分组起一个名字，实现关键字传参
(3) 分发：把每一个app自己的url分发各自的路由文件中

过滤器：
    日期过滤器：{{now|date:"Y/m/d"}}
    若为空则返回内容：{{book_list|default:"没有符合条件的书籍"}}
    截字符结尾三个点表示：{{article|truncatechars:20}}
    截单词结尾三个点表示：{{article|truncatewords:20}}
    不转义(防止js控制客户端)：{{link|safe}}

循环标签：{% for i in list %} 
            <li>{{i}}</li>  要赋值的标签
          {% endfor %}
          
循环计数：forloop.counter，forloop.first(判断是不是第一次循环)
用法： <li>{{forloop.counter}} {{i}}</li>
    
判断：
    {% if num > 100 %}  判断是否大于100   ！！num > 100必须加空格
    <p>100</p>          符合则显示100
    {% else %}
    <p>{{age}}</p>      不符合显示它本身
    {% endif %}
    
变量临时缓存：
    <p>
        {% with name=person.name %}  !!一定不能加空格
        {{name}}
        {% endwith %}
    </p>
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    