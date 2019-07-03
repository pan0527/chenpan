from django.contrib import admin
from .models import *
# Register your models here.

# 在添加书籍的页面添加hero信息
class heroInfoInline(admin.StackedInline):
    # 模型指向
    model = heroInfo
    # 默认自带
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    # 展示内容
    list_display = ("title","pub_date")
    # 过滤内容
    list_filter=["title","pub_date"]
    # 添加搜索框，根据括号里的内容进行修改
    search_fields = ("title","pub_date")
    # 设置每页显示的个数
    list_per_page = 2
    # 内置行，引用关联对象
    inlines = [heroInfoInline,]



admin.site.register(BookInfo,BookInfoAdmin)

class heroInfoAdmin(admin.ModelAdmin):
    # 展示内容
    list_display = ("name", "content","book")
    # 过滤内容
    list_filter = ["name", "content","book"]


admin.site.register(heroInfo,heroInfoAdmin)