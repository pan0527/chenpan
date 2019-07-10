from django import forms
from .models import PollsUser

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,required=True,
                             widget=forms.TextInput(attrs={
                             "name":"username" ,"class":"form-control" ,"id":"username",
                             "placeholder":"请输入名字"})
                             )
    password=forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={
                             "name":"username" ,"class":"form-control" ,"id":"username",
                             "placeholder":"请输入密码"})
                             )

class RegisterForm(forms.ModelForm):
    password1=forms.CharField(label="确认密码",max_length=20,required=True,widget=forms.PasswordInput(attrs={
                              "class":"form-control" ,"id":"password1",
                             "placeholder":"请确认密码"}))
    class Meta:
        model=PollsUser
        fields=["username","password","telephone"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","id":"username", "placeholder":"请输入名字"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","id":"password", "placeholder":"请输入密码"}),
            "telephone":forms.NumberInput(attrs={"labels":"手机号码","class":"form-control","id":"telephone", "placeholder":"请输入手机号码"})

        }
        help_texts={
            "username":""
        }
        labels={
            "telephone":'手机号码'

        }


