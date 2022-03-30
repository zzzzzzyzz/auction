from django.contrib.sites import requests
from django.db.models.fields import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django import forms

from api import models

# 登录验证
from api.models import UserInfo


def logintest(request):
    # print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = models.UserInfo.objects.filter(phone=username).first()
        print(user)
    if username == user.phone and password == user.password:
        return render(request, 'index.html')
    else:
        return HttpResponse("登陆失败！")
    return redirect(request, '/login/')


def register(request):
    return render(request, 'register.html') #注册页面


def login(request):
    return render(request, 'login.html') #登陆页面


def addregister(request):
    # print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password!=password2:
            msg = "密码输入不一致！"
            return render(request,"register.html", {'msg': msg})
        user = UserInfo() #创建一个model实例
        user.phone = username
        user.password = password
        user.save()  #将数据保存在数据库
        return render(request, 'registerSuccess.html') #注册成功，跳转至登录页面
    else:
        return redirect(request, '/register/') #注册不成功，刷新注册页面


def wxlogin(request):
    if request.method =='POST':
        # code = request.POST.get('code')
        # nickname = request.POST.get('nickname')
        req = json.loads(request.body.decode())
        code = req.get('code')
        nickname = req.get('nickname')
        info = {
            'appid': "wx55cca0b94f723dc7",  # 微信小程序
            'secret': "c000e3ddc95d2ef723b9b010f0ae05d5",  # 微信小程序
            'js_code': code,
            'grant_type': "authorization_code",
        }
        result = requests.get(url="https://api.weixin.qq.com/sns/jscode2session", params=info)
        openid = result.json()['openid']
        #token = str(uuid.uuid4())
        exists = models.UserInfo.objects.filter(username=nickname).exists()
        if not exists:
            models.UserInfo.objects.create(
                username=nickname,
                #token = token
                openid=openid
            )
        else:
            models.UserInfo.objects.filter(username=nickname).update(openid=openid)
        return Response({'flag': True})