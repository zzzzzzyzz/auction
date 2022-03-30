from django.db import models

# Create your models here.


class Picture(models.Model):
    picturepath = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='photos', default='user1.jpg')