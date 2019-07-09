# 引用url模块
from django.conf.urls import url
#导入视图函数
from .views import *

app_name="booktest"


urlpatterns=[
    # url('myurl/',myview)
    # url(r'^index/$',index),
    #

    url(r'^$',index,name="index"),
    # url(r'^$',indexView.as_view(),name="index"),

    # url(r'^$',indexTemplateView.as_view(),name="index"),

    # url(r'^list/$',listView.as_view(),name="list"),

    url(r'^list/$',list,name="list"),
    url(r'^detail/(\d+)/$',detail,name="detail"),

    url(r'^deletebook/(\d+)/$',deletebook,name="deletebook"),

    url(r'^addhero/(\d+)/$',addhero,name="addhero"),

    url(r'^deletehero/(\d+)/$',deletehero,name="deletehero"),

    url(r'^addads/$',addads,name="addads"),


]
