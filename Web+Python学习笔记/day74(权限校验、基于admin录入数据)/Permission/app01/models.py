from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField("姓名",max_length=32,)
    pwd = models.CharField("密码",max_length=32,)
    roles = models.ManyToManyField("Role")

    def __str__(self):
        return self.name

class Role(models.Model):

    title = models.CharField("职位",max_length=32)
    permissions = models.ManyToManyField("Permission")

    def __str__(self):
        return self.title

class Permission(models.Model):
    title = models.CharField("权限",max_length=32)
    url = models.CharField(max_length=32)

    def __str__(self):
        return self.title