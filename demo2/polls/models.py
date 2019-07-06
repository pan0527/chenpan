from django.db import models

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
