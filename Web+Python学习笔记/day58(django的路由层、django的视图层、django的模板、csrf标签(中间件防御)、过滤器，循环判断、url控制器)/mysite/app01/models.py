from django.db import models

# Create your models here.
#存放表结构

class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)  #999999.99 共8位，2位浮点型
    publish = models.CharField(max_length=32)
    pub_date = models.DateTimeField()   #"2012-12-12"













