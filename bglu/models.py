from django.db import models

# Create your models here.


class bloodglu(models.Model):
     name = models.CharField(max_length=64)
     age = models.IntegerField(max_length=10)
     gender = models.CharField(max_length=10)#性别
     Mbglu = models.CharField(max_length=10) #早上血糖
     Abglu = models.CharField(max_length=10) #中午血糖
     Nbglu = models.CharField(max_length=10) #晚上血糖