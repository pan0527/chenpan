# 引用url模块
from django.conf.urls import url
#导入视图函数
from .views import *
urlpatterns=[
    # url('myurl/',myview)
    url(r'^index/$',index),
    url(r'^list/$',list),
    url(r'^detail/$',detail)
]
