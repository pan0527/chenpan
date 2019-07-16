from django.conf.urls import url
from .views import *

app_name="education"

urlpatterns=[
    url(r'^register/$',register,name="register"),
    url(r'^login/$',login,name="login"),
    url(r'^index/$',index,name="index"),

]