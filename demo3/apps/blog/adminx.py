from .models import *
import xadmin
xadmin.site.register(Tag)
xadmin.site.register(Article)
xadmin.site.register(Ads)
xadmin.site.register(Category)
