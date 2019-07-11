from django.conf.urls import url,include
from .views import *
app_name="blog"

urlpatterns=[
    url(r'^$',index,name="index"),
    url(r'^single/(\d+)/$',single,name="single"),
    url(r'^addarticle/$',addarticle,name="addarticle")

]
