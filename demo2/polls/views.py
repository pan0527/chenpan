from django.shortcuts import render,redirect,reverse,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import Question,Choices,PollsUser


from django.contrib.auth import login as lgn ,logout as lgt,authenticate
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
        username=request.POST.get("username")
        password = request.POST.get("password")
        user=PollsUser.objects.create_user(username=username,password=password)
        if user:
            return redirect(reverse("polls:login"))
        else:
            return render(request,"polls/login.html",{"errors":"注册失败"})

def login(request):
    if request.method=="GET":
       return render(request,"polls/login.html")
    elif request.method=="POST":
        #3.使用django自带的User
        username = request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            lgn(request,user)
            return redirect(reverse("polls:index"))
        else:
            return render(request,"polls/login.html")

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



