
"""
自定义模板表达式
扩展django原有功能
在模板中直接使用

"""

from django.template import library
register=library.Library()
from blog.models import Article

@register.simple_tag
def getlatestarticles(num):
    return Article.objects.order_by("-create_time")[:num]



