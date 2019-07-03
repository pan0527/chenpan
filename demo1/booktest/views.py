from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 视图函数
# def myview(request):
#     return HttpResponse("这是自定义展示路由")index
def index(request):
    return HttpResponse("这是首页 <a href='/booktest/list/'>跳转到列表页</a>" )

def list(request):
    return HttpResponse("这是列表页 <a href='/booktest/detail/'>跳转到详情页页</a>")

def detail(request):
    return HttpResponse("这是详情页 <a href='/booktest/index/'>跳转到首页</a>")