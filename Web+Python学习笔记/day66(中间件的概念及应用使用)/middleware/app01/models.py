from django.db import models

# Create your models here.
class IP_count(models.Model):
    IP = models.CharField(max_length=30)
    count = models.IntegerField()