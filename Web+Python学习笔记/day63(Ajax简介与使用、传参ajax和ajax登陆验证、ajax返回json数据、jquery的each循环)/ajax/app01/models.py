from django.db import models

# Create your models here.
class UserIngo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

class Class(models.Model):
    cid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=30)
    grade = models.ForeignKey(to="Class_grade",on_delete=models.CASCADE)

class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    clas = models.ForeignKey(to="Class",on_delete=models.CASCADE)

class Teacher(models.Model):
    tid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=30)

class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)
    teacher = models.ForeignKey(to="Teacher",on_delete=models.CASCADE)

class Scoree(models.Model):
    sid = models.AutoField(primary_key=True)
    student = models.ForeignKey(to='Student',on_delete=models.CASCADE)
    course = models.ForeignKey(to='Course', on_delete=models.CASCADE)
    score = models.IntegerField()

class Class_grade(models.Model):
    gid = models.AutoField(primary_key=True)
    gname = models.CharField(max_length=30)

class Teach_class(models.Model):
    tcid = models.AutoField(primary_key=True)
    tid = models.ForeignKey(to='Teacher',on_delete=models.CASCADE)
    cid = models.ForeignKey(to='Class',on_delete=models.CASCADE)








