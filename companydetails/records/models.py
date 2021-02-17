
from django.db import models
class Position(models.Model):
    tittle=models.CharField(max_length=30)
    def __str__(self):
        return self.tittle
class employee1(models.Model):
    name=models.TextField(null=True,blank=True)
    empcode=models.CharField(default='inactive',max_length=10)
    position=models.ForeignKey(Position,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# Create your models here.
