from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse
from django.views.static import serve
from .forms import ArticleForm
from django.core.paginator import Paginator,Page
# Create your views here.

def index(request):
    ads=Ads.objects.all()
    articles=Article.objects.all()
    # paginator=Paginator(articles,1)
    # print(paginator.object_list)#文章对象P
    # print(paginator.count) #文章数
    # print(paginator.num_pages) #几页
    # print(paginator.page_range) #页码范围
    # page=paginator.get_page(2)
    # print(page) #当前处于第几页
    # print(page.paginator is paginator) #True
    # print(page.object_list) #当前页的文章
    # print(page.number) #当前页码
    # print(page.next_page_number()) #下个页码
    # print(page.previous_page_number()) #先前页码
    # print(page.has_next()) #是否有下一页
    # print(page.has_previous()) #是否有上一页
    pagenum=request.GET.get("page")
    pagenum=1 if not pagenum else pagenum
    page=Paginator(articles,1).get_page(pagenum)
    print(page)
    return render(request,"blog/index.html",{"page":page})

def single(request,id):
    if request.method=="GET":
        return render(request,"blog/single.html")
    elif request.method=="POST":
        return render(reverse("blog:single"))
def addarticle(request):
    if request.method=="GET":
        af=ArticleForm()
        return render(request,"blog/addarticle.html",locals())
    elif request.method=="POST":
        af=ArticleForm(request.POST)
        if af.is_valid():
            article=af.save(commit=False)
            article.category=Category.objects.first()
            article.author=User.objects.first()
            article.save()
            return redirect(reverse("blog:index"))
        else:
            return HttpResponse("添加失败")
