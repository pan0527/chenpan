
from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# Create your models here.

# 轮播图
class Ads(models.Model):
    img = models.ImageField(upload_to="Ads")
    desc = models.CharField(max_length=20)
    def __str__(self):
        return self.desc
# 用户表
class Students(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    email=models.EmailField()
    def __str__(self):
        return self.username

#教师表
class Teachers(User):
    # 职业
    occupation=models.CharField(max_length=10)
    student=models.ManyToManyField(Students)
    img = models.ImageField(upload_to="teacher",null=True)

# 课程分类
class CourseCategory(models.Model):
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title

# 课程表
class Course(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=200)
    img = models.ImageField(upload_to="course",null=True)
    price=models.FloatField(default=0.0)
    content=models.TextField()
    type = models.CharField(max_length=10, choices=(("online", "线上"), ("underline", "线下")), default="online")
    teacher=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    student = models.ManyToManyField(Students)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#课程评论
class CourseComment(models.Model):
    title = models.CharField(max_length=10)
    content=models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    score=models.IntegerField(default=5)
    student=models.ManyToManyField(Students)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

# blog部分
# 分类
class BlogCategory(models.Model):
    title=models.CharField(max_length=10)
    def __str__(self):
        return self.title

# 标签
class BlogTag(models.Model):
    title=models.CharField(max_length=10)
    def __str__(self):
        return self.title
# 文章
class Article(models.Model):
    title=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    author=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    views=models.IntegerField(default=0)
    # body=models.TextField()
    # 不能添加图片
    # body=UEditorField()
    # 添加图片，加参数
    body = UEditorField(imagePath="articleimg/",width="100%")
    tags=models.ManyToManyField(BlogTag)
    def __str__(self):
        return self.title

# 评论
class BlogComment(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    url=models.URLField(blank=True,null=True,default="http://www.baidu.com")
    content=models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    def __str__(self):
        return self.name




