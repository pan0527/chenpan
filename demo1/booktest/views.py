from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo,heroInfo
# Create your views here.
# 视图函数
# def myview(request):
#     return HttpResponse("这是自定义展示路由")index
def index(request):
    # 1.获取模板
    # temp1=loader.get_template("booktest/index.html")
    # 2.使用字典渲染字典参数
    # result1=temp1.render({"username":'tom'})
    # 3.返回
    # return HttpResponse(result1)
    # return HttpResponse("这是首页 <a href='/booktest/list/'>跳转到列表页</a>" )
    return render(request,"booktest/index.html",{"username":"tom"})

def list(request):
    # 1.获取模板
    # temp2= loader.get_template("booktest/list.html")
    # 2.使用字典渲染字典参数
    books=BookInfo.objects.all
    # result2 = temp2.render({"books":books})
    # 3.返回
    # return HttpResponse(result2)
    return render(request,"booktest/list.html",{"books":books})
    # s="""
    # <br>
    # <a href='/booktest/detail/1/'>跳转到详情页页1</a>
    # <br>
    # <a href='/booktest/detail/2/'>跳转到详情页页2</a>
    # <br>
    # <a href='/booktest/detail/3/'>跳转到详情页页3</a>
    # """
    # return HttpResponse("这是列表页%s "%(s,))


def detail(request,id):
    # 1.获取模板
    # temp3= loader.get_template("booktest/detail.html")
    # 2.使用字典渲染字典参数
    book=BookInfo.objects.get(pk=id)
    # result3 = temp3.render({"book":book})
    # 3.返回
    # return HttpResponse(result3)
    return render(request,"booktest/detail.html",{"book":book})
    # return HttpResponse("这是详情页%s <a href='/booktest/index/'>跳转到首页</a>"%(id,))