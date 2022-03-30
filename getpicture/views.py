import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from auction import settings
from getpicture.models import Picture


def upload(request):
    if request.method == "POST":
        print(request.method)
        picture = request.FILES.get('pic')
        fname = '%s/picture/%s' % (settings.MEDIA_ROOT, picture.name) #路径为static/media/picture/
        with open(fname, 'wb') as pic:  #将图片写入该路径
            for c in picture.chunks():
                pic.write(c)
        pic = Picture()
        pic.picturepath = 'picture/%s' % picture.name #将相对路径保存在数据库
        pic.photo = picture.name
        pic.save() #保存数据库
        return HttpResponse('上传成功！')
    return render(request, 'getPicture.html')


# 返回上传图片的页面
def getUpload(request):
    return render(request, 'getPicture.html')