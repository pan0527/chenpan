
"""
自定义模板表达式
扩展django原有功能
在模板中直接使用

"""

from django.template import library
register=library.Library()
from blog.models import Article,Category,Tag

@register.simple_tag
def getlatestarticles(num):
    return Article.objects.order_by("-create_time")[:num]

# 定义自己的过滤器
@register.filter
def mylower(value):
    return value.lower()

#归档模板标签
@register.simple_tag
def gettimes(num):
    times=Article.objects.dates("create_time", "month")
    # print(times)#<QuerySet [datetime.date(2017, 8, 1), datetime.date(2018, 8, 1), datetime.date(2019, 7, 1)]>
    return times

#分类模板标签
@register.simple_tag
def getcategory():
    category=Category.objects.all()
    return category

#标签云模板标签
@register.simple_tag
def gettags():
    tags=Tag.objects.all()
    return tags


