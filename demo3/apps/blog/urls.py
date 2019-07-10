from django.conf.urls import url,include
from .views import *
app_name="blog"

urlpatterns=[
    url(r'^index/$',index,name="index"),

]
