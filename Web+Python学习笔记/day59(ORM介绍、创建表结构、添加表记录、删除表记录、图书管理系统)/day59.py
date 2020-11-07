ORM：object relation mapping

类--------------表
类属性----------表字段
类对象----------表记录

数据库迁移：django会把srttings中
            的INSTALLED_APPS中的每一个应用中的models对应类创建成数据库中的表

python manage.py makemigrations
python manage.py migrate
from django.db.utils import IntegrityError
添加表数据：
    Book.id   #打印当前生成表对象，Book为创建的类

    # 方式1
    book = Book(title="西游记",price=50,pub_date=now,publish="人民出版社")
    book.save()
    
    #方式2
    Book.objects.create(title="Web开发",price=250,pub_date=now,publish="清华大学出版社")