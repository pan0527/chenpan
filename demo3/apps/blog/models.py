from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#轮播图
class Ads(models.Model):
    img=models.ImageField(upload_to="Ads")
    desc=models.CharField(max_length=20)
    index=models.IntegerField(default=0)

# 分类
class Category(models.Model):
    title=models.CharField(max_length=10)
    def __str__(self):
        return self.title

# 标签
class Tag(models.Model):
    title=models.CharField(max_length=10)
    def __str__(self):
        return self.title
# 文章
class Article(models.Model):
    title=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return self.title








