from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.
# 注册
def register(request):
    if request.method=="GET":
        return render(request,"education/register.html")
    elif request.method=="POST":
        pwd=request.POST.get("pwd")
        pwd1 = request.POST.get("pwd1")
        if pwd==pwd1:
            user_email = request.POST.get("user_email")
            user_name = request.POST.get("user_name")
            user=Students.objects.filter(username=user_name).first()
            print(user)
            if not user:
                student=Students()
                student.username=user_name
                student.password=pwd
                student.email=user_email
                student.save()
                return redirect(reverse("education:login"))
            else:
                return render(request, "education/register.html", {"error": "用户名已存在"})
        else:
            return render(request, "education/register.html", {"error": "两次密码不同"})

# 登录
def login(request):
    if request.method == "GET":
        return render(request, "education/login.html")
    elif request.method=="POST":
        username=request.POST.get("name")
        password=request.POST.get("pwd")
        user=Students.objects.filter(username=username,password=password).first()
        print(user)
        if user:
            return render(request,"education/index.html")
        else:
            return render(request,"education/login.html",{"error": "用户或密码错误"})
# 首页
def index(request):
    return render(request, "education/index.html")
