from django.conf.urls import url
from .views import *
app_name="polls"

urlpatterns=[

    url(r'^index/$',index,name="index"),
    url(r'^detail/(\d+)/$',detail,name="detail"),
    url(r'^result/(\d+)/$',result,name="result"),
    url(r'^login/$',login,name="login"),
    url(r'^logout/$',logout,name="logout"),
    url(r'^register/$',register,name="register"),
    url(r'^verify/$',verify,name="verify"),
    url(r'^active/(\d+)/$',active,name="active"),

]