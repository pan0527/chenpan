from django.conf.urls import url
from .views import *

app_name="education"

urlpatterns=[
    url(r'^register/$',register,name="register"),
    url(r'^login/$',login,name="login"),
    url(r'^index/$',index,name="index"),
    url(r'^courses/$',courses,name="courses"),
    url(r'^coursesingle/(\d+)/$',coursesingle,name="coursesingle"),
    url(r'^teacher/$',teacher,name="teacher"),
    url(r'^teachersingle/(\d+)/$',teachersingle,name="teachersingle"),
    url(r'^blog/$',blog,name="blog"),
    url(r'^single/(\d+)/$',single,name="single"),
    url(r'^addcomment/(\d+)/$',addcomment,name="addcomment"),
    url(r'^getcategory/(\d+)/$',getcategory,name="getcategory"),
    url(r'^gettag/(\d+)/$',gettag,name="gettag"),
    url(r'^getfile/(\d+)/(\d+)/$',getfile,name="getfile"),
    url(r'^getauthor/(\d+)/$',getauthor,name="getauthor"),
    url(r'^getvedio/(\d+)/$', getvedio, name="getvedio"),
    url(r'^coursecategory/(\d+)/$',coursecategory,name="coursecategory"),
    url(r'^allcoursecategory/$',allcoursecategory,name="allcoursecategory"),






]