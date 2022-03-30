from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from bglu import models
from bglu.models import bloodglu


def glu(request):
    return render(request, 'Bloodglu.html')


def getGlu(request):
    if request.method == "POST":
        print(request.method)
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("sex")
        Mglu = request.POST.get("Mglu")
        Aglu = request.POST.get("Aglu")
        Nglu = request.POST.get("Nglu")
        print(gender)
        glu = bloodglu()
        glu.name = name
        glu.age = age
        glu.gender = gender
        glu.Mbglu = Mglu
        glu.Abglu = Aglu
        glu.Nbglu = Nglu
        glu.save()
        return redirect('/bglu/showList/')


#查询全部
def showList(request):
    bglulist = models.bloodglu.objects.all()
    print(bglulist)
    return render(request, 'show.html', {'namelist': bglulist})


#增加数据
# def addbglu(request):
#     models.bloodglu.objects.create(name='zyz', age='10', gender='1', Mbglu='32', Abglu='18', Nbglu='55')
#     bglulist = models.bloodglu.objects.all()
#     print(bglulist)
#     return render(request, 'show.html', {'namelist': bglulist})


#删除数据
def deleteglu(request):
    if request.method=='GET':
        name = request.GET.get('name')
        print(name)
        models.bloodglu.objects.filter(name=name).delete()
        namelist = models.bloodglu.objects.all()
    return render(request, 'show.html', {'namelist': namelist})


#修改数据
def updateglu(request):
    if request.method=='GET':
        name = request.GET.get('name')
        userbglu = models.bloodglu.objects.filter(name=name)
    return render(request, 'update.html', {'userbglu': userbglu})


def getGluupdate(request):
    if request.method == "POST":
        print(request.method)
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("sex")
        Mglu = request.POST.get("Mglu")
        Aglu = request.POST.get("Aglu")
        Nglu = request.POST.get("Nglu")
        models.bloodglu.objects.filter(name=name).update(age=age, gender=gender, Mbglu=Mglu, Abglu=Aglu, Nbglu=Nglu)
    return redirect('/bglu/showList/')