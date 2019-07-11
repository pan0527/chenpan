from .models import *
import xadmin
xadmin.site.register(Tag)
# ArticleAdmin不需要继承任何类
class ArticleAdmin:
    # 指定模型类的某个字段使用ueditor样式
    style_fields={"body":"ueditor"}

xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Ads)
xadmin.site.register(Category)
