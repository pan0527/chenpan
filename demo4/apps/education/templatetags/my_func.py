from django.template import library
from education.models import *
register=library.Library()

#分类模板标签
@register.simple_tag
def getcategory(num):
    category=BlogCategory.objects.all()
    # print(category)
    return category
#标签云模板标签
@register.simple_tag
def gettag():
    return BlogTag.objects.all()
#过滤日期模板标签
@register.simple_tag
def getdate():
    return  Article.objects.dates("create_time", "month")
# 作者模板标签
@register.simple_tag
def getauthor(num):
    return Teachers.objects.all()[:num]



