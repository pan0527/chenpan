from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Question,Choices
# Create your views here.
# 视图函数
def index(request):
    questions=Question.objects.all
    return render(request,"polls/index.html",{"questions":questions})

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

def result(request,id):
    question=Question.objects.get(pk=id)
    return render(request, "polls/result.html", {"question": question})
