from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator,Page
from django.http import JsonResponse
# Create your views here.
# 封装了一个方法
def getpage(request,object_list,per_num):
    pagenum = request.GET.get("page")
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    return page

# 装饰器
def checkout(fun):
    def check(request,*args):
        username=request.session.get('username')
        # print(username)
        # if request.user and request.user.is_authenticated:
        if username:
            return fun(request,*args)
        else:
            return redirect(reverse('education:login'))
    return check

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
        if user:
            request.session['username']=username
            return redirect(reverse("education:index"))
        else:
            return render(request,"education/login.html",{"error": "用户或密码错误"})
# 首页
def index(request):
    courses = Course.objects.all()

    return render(request, "education/index.html",locals())
# 课程
def courses(request):
    courses=Course.objects.all()
    coursescategory=CourseCategory.objects.all()
    page=getpage(request,courses, 6)
    return render(request, "education/courses.html",{"coursescategory":coursescategory,"page":page})
# 课程详情页
def coursesingle(request,id):
    course=Course.objects.get(pk=id)
    return render(request,"education/coursesingle.html",{"course":course})
# 教师
def teacher(request):
    teachers=Teachers.objects.all()
    page = getpage(request, teachers, 8)
    return render(request, "education/teacher.html", {"page": page})
# 教师详情页
def teachersingle(request,id):
    teacher=Teachers.objects.get(pk=id)
    courses=teacher.course_set.all()
    page = getpage(request, courses, 4)
    return render(request,"education/teachersingle.html",{"teacher":teacher,"page":page})
#博客
def blog(request):
    ads = Ads.objects.all()
    articles = Article.objects.all()
    page = getpage(request, articles, 3)
    return render(request, "education/blog.html",{"ads":ads,"page":page})
#博客详情页
def single(request,id):
    article = Article.objects.get(pk=id)
    return render(request, "education/single.html",locals())
# 添加评论
def addcomment(request,id):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        url = request.POST.get("url")
        content = request.POST.get("content")
        c = BlogComment()
        c.name = name
        c.email = email
        c.url = url
        c.content = content
        c.article = Article.objects.get(pk=id)
        c.save()
        return JsonResponse({"name": c.name, "content": c.content, "create_time": c.create_time})
# 博客分类
def getcategory(request,id):
    if request.method == "GET":
        category = get_object_or_404(BlogCategory,pk=id)
        articles = category.article_set.all()
        page = getpage(request, articles, 2)
    return render(request, "education/blog.html", {"page":page})

# 博客标签云
def gettag(request,id):
    if request.method == "GET":
        tags = get_object_or_404(BlogTag,pk=id)
        articles = tags.article_set.all()
        page = getpage(request, articles, 2)
    return render(request, "education/blog.html", {"page":page})
# 归档
def getfile(request,year,month):
    if request.method == "GET":
        articles = Article.objects.filter(create_time__year=year, create_time__month=month)
        page = getpage(request, articles, 2)
    return render(request, "education/blog.html", {"page":page})
# 作者
def getauthor(request,id):
    if request.method == "GET":
        teachers = get_object_or_404(Teachers,pk=id)
        articles = teachers.article_set.all()
        page = getpage(request, articles, 2)
    return render(request, "education/blog.html", {"page":page})
# 视频
@checkout
def getvedio(request,id):
    if request.method == "GET":
        vedio=Vedio.objects.get(pk=id)
        return render(request, "education/vedio.html",{'vedio':vedio})

# 课程分类
def coursecategory(request,id):
    category = CourseCategory.objects.get(pk=id)
    courses = category.course_set.all()
    # print(courses,type(courses))
    courselist = []
    for i in courses:
        course = {
            'id':i.id,
            'name':i.name,
            'teacher':i.teacher.username,
            'tid':i.teacher.id,
            'img':str(i.img),
            'price':i.price,
        }
        courselist.append(course)
    # print(courselist)
    return JsonResponse(courselist,safe=False)

def allcoursecategory(request):
    courses = Course.objects.all()
    courselist = []
    for i in courses:
        course = {
            'id': i.id,
            'name': i.name,
            'teacher': i.teacher.username,
            'tid': i.teacher.id,
            'img': str(i.img),
            'price': i.price,
        }
        courselist.append(course)
    # print(courselist)
    return JsonResponse(courselist, safe=False)
# 异步刷新分页
# def getallcoursepage(request):
#     courses = Course.objects.all()
#     page = getpage(request, courses, 6)
#     # print(page)
#     courselist = []
#     print(page.object_list,len(page.object_list))
#     for i in page.object_list:
#         print("+++++++++++")
#         print(i.id)
#         course = {
#             'id': i.id,
#             'name': i.name,
#             'teacher': i.teacher.username,
#             'tid': i.teacher.id,
#             'img': str(i.img),
#             'price': i.price,
#         }
#         # courselist.append(course)
#     # print(courselist,len(courselist))
#     return JsonResponse(courselist, safe=False)
