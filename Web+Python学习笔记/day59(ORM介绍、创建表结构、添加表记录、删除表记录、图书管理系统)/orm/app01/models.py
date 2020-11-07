from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    pub_date = models.DateTimeField()  #2012-12-12
    price = models.DecimalField(max_digits=8, decimal_places=2) #999999.99
    publish = models.CharField(max_length=32)

    def __str__(self):     #使用这个函数打印结果会返回[<Book:title>]
        return self.title