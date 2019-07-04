
from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import BookInfo,heroInfo
from django.views.generic import View,TemplateView,ListView

# Create your views here.
# 视图函数
# def myview(request):
#     return HttpResponse("这是自定义展示路由")index


class indexView(View):
    # 重写request的get方法
    def get(self,request):
        return render(request,"booktest/index.html",{"username":"tom"})

class indexTemplateView(TemplateView):
    template_name ="booktest/index.html"
    def get_context_data(self):
        return {"username":"tom"}

class listView(ListView):
    model = BookInfo
    template_name = "booktest/list.html"
    context_object_name = "books"
    # def get_queryset(self):
    #     return BookInfo.objects.all()



def index(request):
    # 1.获取模板
    # temp1=loader.get_template("booktest/index.html")
    # 2.渲染字典参数
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

def deletebook(request,id):
    book=BookInfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse("booktest:list"))
    # return HttpResponse("删除成功")


def addhero(request,id):
    book = BookInfo.objects.get(pk=id)
    if request.method=="GET":
        return render(request,"booktest/addhero.html",{"book":book})
    elif request.method=="POST":
        name=request.POST.get("username")
        content=request.POST.get("content")
        gender=request.POST.get("gender")
        gender1=request.POST.get("gender1")
        # 构造一个hero对象
        hero=heroInfo()
        hero.name=name
        hero.content=content
        hero.book=book
        hero.gender=gender
        hero.type=gender1
        hero.save()
        # return HttpResponse("添加成功")
        return redirect(reverse("booktest:detail",args=(id,)))

def deletehero(request,id):

    hero=heroInfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    # return HttpResponse("删除成功")
    # return HttpResponseRedirect("/detail/"+str(bookid)+"/")
    # result=reverse("booktest:detail",args=(bookid,))
    # print(result)
    return redirect(reverse("booktest:detail",args=(bookid,)))



"""
正常请求：一次请求响应一次
重定向：发起一次请求302 在处理过程中再次发起请求 返回响应200
"""
