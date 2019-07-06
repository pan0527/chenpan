from django.db import models

# Create your models here.
class BookInfo(models.Model):
    title=models.CharField(max_length=20)
    pub_date=models.DateField(auto_now=True)
    def __str__(self):
        return self.title

# 定义自己的管理器类,继承了models.Manager，又添加了新的方法
class HeroInfoManager(models.Manager):
    def addhero(self,_name,_content,_book,_gender,_gender1):
        # 构造一个hero对象
        hero = heroInfo()
        hero.name = _name
        hero.content = _content
        hero.book = _book
        hero.gender = _gender
        hero.type = _gender1
        hero.save()

class heroInfo(models.Model):
    name=models.CharField(max_length=20)
    # gender=models.BooleanField(default=True)
    gender=models.CharField(max_length=5,choices=(  ("man","男"),("woman","女") ))
    type=models.CharField(max_length=5,choices=( ("man","男"),("woman","女") ),default="man")
    content=models.CharField(max_length=100)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    objects=HeroInfoManager()

    def __str__(self):
        return self.name

class Account(models.Model):
    name=models.CharField(max_length=10)

class Contract(models.Model):
    telephone=models.CharField(max_length=11)
    acc=models.OneToOneField(Account,on_delete=models.CASCADE)

class Host(models.Model):
    name=models.CharField(max_length=10)

class Application(models.Model):
    name=models.CharField(max_length=10)
    h=models.ManyToManyField(Host)

