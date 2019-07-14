from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import *
from django.http import HttpResponse
from django.views.static import serve
from .forms import ArticleForm,CommentForm
from django.core.paginator import Paginator,Page
# Create your views here.
# 封装了一个方法
def getpage(request,object_list,per_num):
    pagenum = request.GET.get("page")
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    return page


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
    # print(page)
    return render(request,"blog/index.html",{"page":page,"ads":ads})

def single(request,id):
    if request.method=="GET":
        article=get_object_or_404(Article,pk=id)
        cf=CommentForm()
        return render(request,"blog/single.html",{"article":article,"cf":cf})
    elif request.method=="POST":
        cf=CommentForm(request.POST)
        comment=cf.save(commit=False)
        article=get_object_or_404(Article,pk=id)
        comment.article=article
        comment.save()
        return redirect(reverse("blog:single",args=(article.id,)))

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

# 归档
def file(request,year,month):
    if request.method=="GET":
        articles = Article.objects.filter(create_time__year=year, create_time__month=month)
        pagenum=request.GET.get("page")
        pagenum=1 if not pagenum else pagenum
        page=Paginator(articles,1).get_page(pagenum)
        return render(request,"blog/index.html",{'page':page})

# 分类
def category(request,id):
    if request.method == "GET":
        category = get_object_or_404(Category,pk=id)
        articles = category.article_set.all()
        pagenum = request.GET.get("page")
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(articles, 1).get_page(pagenum)
        return render(request,'blog/index.html',{"page":page})

# 标签云
def gettag(request,id):
    if request.method == "GET":
        tags= get_object_or_404(Tag,pk=id)
        articles = tags.article_set.all()
        pagenum = request.GET.get("page")
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(articles, 1).get_page(pagenum)
        return render(request,'blog/index.html',{"page":page})





