from django.shortcuts import render,redirect,reverse,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import Question,Choices,PollsUser
from .forms import *
import random,io
from PIL import Image,ImageDraw,ImageFont
from django.core.cache import cache
from django.contrib.auth import login as lgn ,logout as lgt,authenticate
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
# Create your views here.
# 视图函数

# 装饰器
def checkout(fun):
    def check(request,*args):
        # username = request.COOKIES.get("username")
        # username=request.session['username']
        # print(username)
        if request.user and request.user.is_authenticated:
        # if username:
            return fun(request,*args)
        else:
            return redirect(reverse('polls:login'))
    return check


@checkout
def index(request):

    print(request.user,request.user.is_authenticated) #request.user为匿名用户,is_authenticated 用户是否被授权

    questions=Question.objects.all()
    # session
    # username=request.session['username']
    # cookie
    # username = request.COOKIES.get("username")
    return render(request,"polls/index.html",{"questions":questions})
    # user=request.COOKIES.get("username")
    # if user:
    #     questions=Question.objects.all
    #     return render(request,"polls/index.html",{"questions":questions,"user":user})
    # else:
    #     return redirect(reverse('polls:login'))
@checkout
def detail(request,id):
    question = Question.objects.get(pk=id)
    if request.method=="GET":
        return render(request,"polls/detail.html",{"question":question})
    elif request.method=="POST":
        choiceid=request.POST.get("ce")
        choice=Choices.objects.get(pk=choiceid)
        choice.votes+=1
        choice.save()
        return redirect(reverse("polls:result",args=(id,)))

@checkout
def result(request,id):
    question=Question.objects.get(pk=id)
    return render(request, "polls/result.html", {"question": question})



def register(request):
    if request.method=="POST":
        rm = RegisterForm(request.POST)

        if rm.is_valid():
            # 先返回一个user 此时没有保存数据库应为密码还没有加密
            user=rm.save(commit=False)
            # 对user用户设置密码 加密过得密码
            user.set_password(rm.cleaned_data['password'])
            # 保存数据库
            user.is_active=False
            user.save()
            # recipient_list=[rm.cleaned_data['email']]
            recipient_list = ["15713872361@163.com", ]
            try:
                # send_mail("django学习","这是一封邮件",settings.EMAIL_HOST_USER,recipient_list)
                mail = EmailMultiAlternatives("django学习html", "<a href='http://127.0.0.1:8000/polls/active/%s/'>点我激活</a>"%(user.id,), settings.EMAIL_HOST_USER,
                                              recipient_list)
                mail.content_subtype = "html"
                mail.send()
                print("send success")
            except Exception as e:
                print(e)
            return redirect(reverse("polls:login"))
        else:
            lf = LoginForm()
            rm = RegisterForm()
            return render(request, 'polls/login.html', {"errors": "注册失败", "lf":lf,"rm":rm})

        # username=request.POST.get("username")
        # password = request.POST.get("password")
        # user=PollsUser.objects.create_user(username=username,password=password)
        # if user:
        #     return redirect(reverse("polls:login",))
        # else:
        #     return render(request,"polls/login.html",{"errors":"注册失败"})

def login(request):
    if request.method=="GET":

        lf = LoginForm()
        rm = RegisterForm()
        return render(request,"polls/login.html",{"lf":lf,"rm":rm})
    elif request.method=="POST":
        #3.使用django自带的User
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # 利用django自带表单类创建表单，获取表单数据
        verifycode=request.POST.get("verify")
        if not verifycode==cache.get("verify"):
            return HttpResponse("验证码错误")

        lf=LoginForm(request.POST)
        if lf.is_valid():
            username=lf.cleaned_data.get("username")
            password=lf.cleaned_data.get("password")
            user=PollsUser.objects.filter(username=username).first()
            print(user)
            if user.check_password(password):
                # user=authenticate(request,username=username,password=password)
                if user:
                    if user.is_active:
                        lgn(request,user)
                        return redirect(reverse("polls:index"))
                    else:
                        return render(request,"polls/login.html",{"errors":"用户为激活"})
                else:
                    lf = LoginForm()
                    rm = RegisterForm()
                    return render(request,"polls/login.html",{"errors":"登录失败","lf":lf,"rm":rm})

        # 检测用户名、密码是否对应
        # 1.使用cookie存贮
        # username=request.POST.get("username")
        # response=redirect(reverse('polls:index'))
        # response.set_cookie("username",username)
        # return response

        #2.使用sessions
        # request.session['username']=request.POST.get("username")
        # return redirect(reverse("polls:index"))

def logout(request):
    # 1.cookies
    # response = redirect(reverse('polls:login'))
    # response.delete_cookie("username")
    # return response
    #2.session
    # request.session.flush()
    # 3.使用django自带的User
    lgt(request)

    return redirect(reverse("polls:login"))

def verify(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    cache.set("verify",rand_str)
    # 构造字体对象
    font = ImageFont.truetype('ARLRDBD.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')

def active(request,id):
    user=get_object_or_404(PollsUser,pk=id)
    user.is_active=True
    user.save()
    return redirect(reverse("polls:login"))



