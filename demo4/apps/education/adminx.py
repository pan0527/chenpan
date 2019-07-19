import xadmin
from .models import *

class ArticleAdmin:
    style_fields = {"body": "ueditor"}
xadmin.site.register(Article, ArticleAdmin)

xadmin.site.register(Students)
xadmin.site.register(Teachers)
xadmin.site.register(CourseCategory)
xadmin.site.register(Course)
xadmin.site.register(CourseComment)
xadmin.site.register(BlogCategory)
xadmin.site.register(BlogTag)
xadmin.site.register(BlogComment)
xadmin.site.register(Ads)
xadmin.site.register(Vedio)
