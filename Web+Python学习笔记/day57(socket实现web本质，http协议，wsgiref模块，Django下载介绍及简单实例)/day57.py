使用web框架的流程:
	1 urls 定义映射关系("timer",timer)
	
	2 创建视图函数：
    def timer(evsion):
        业务逻辑
        
        return 文件(templates文件夹中)
    
    3 一旦涉及数据库操作，使用models
    
1 下载django：pip install django
2 创建django项目：django-admin startproject 项目名称
3 创建应用  python manage.py startapp app名称
4 启动项目  python manage.py runserver IP:PORT

项目名称
    --manage.py  
    --项目名称
        --settings.py：配置信息
        --urls：路径与视图函数的映射
        --wsgi：封装scoket
        
    app01
        --models：存放与该app相关的表结构
        --view：存放与该app相关的视图函数
        
项目与应用

1 django的url控制器
2 django的视图
3 django的模板（template）
4 ORM

web应用：https://www.cnblogs.com/yuanchenqi/articles/8869302.html
http协议：https://www.cnblogs.com/yuanchenqi/articles/8875623.html
web框架：https://www.cnblogs.com/yuanchenqi/articles/8946917.html
Django简介：https://www.cnblogs.com/yuanchenqi/articles/8875659.html
Django-1的路由层：https://www.cnblogs.com/yuanchenqi/articles/8876685.html
Django的视图层：https://www.cnblogs.com/yuanchenqi/articles/8876856.html
Django的模板层：https://www.cnblogs.com/yuanchenqi/articles/8876892.html



