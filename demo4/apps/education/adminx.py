from .models import *
import xadmin
xadmin.site.register(Students)
xadmin.site.register(Teachers)
xadmin.site.register(CourseCategory)
xadmin.site.register(Course)
xadmin.site.register(CourseComment)
xadmin.site.register(BlogCategory)
xadmin.site.register(BlogTag)
xadmin.site.register(Article)
xadmin.site.register(BlogComment)

