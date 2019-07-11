from  django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=["title","body"]
        widgets={
            'title':forms.TextInput(attrs={"class":"form-control"}),
        }
        labels={
            'title':"标题",
            'body':'内容',
        }





