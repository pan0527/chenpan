from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    desc= models.CharField(max_length=50)
    desc_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.desc

class Choices(models.Model):
    desc=models.CharField(max_length=50)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return self.desc
# 继承django自带的User表
class PollsUser(User):
    telephone=models.CharField(max_length=11)



