from django.db import models

# Create your models here.


class UserInfo(models.Model):
    phone = models.CharField(max_length=11,unique=True)
    password = models.CharField(max_length=64, null=True,blank=True)