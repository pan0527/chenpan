from django.conf.urls import url,include
from .views import *
from . import  feed
app_name="blog"

urlpatterns=[
    url(r'^$',index,name="index"),
    url(r'^single/(\d+)/$',single,name="single"),
    url(r'^addarticle/$',addarticle,name="addarticle"),

    url(r'^file/(\d+)/(\d+)/$',file,name="file"),
    url(r'^rss/$',feed.BlogFeed(),name="rss"),
    url(r'^category/(\d+)/$',category,name="category"),
    url(r'^gettag/(\d+)/$',gettag,name="gettag"),

]
