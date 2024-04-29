from django.db import models
from django.contrib.auth.admin import User
# Create your models here.

class Board(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.TextField(max_length=150)
    def __str__(self):
        return self.name
class Topic(models.Model):
    subject=models.CharField(max_length=255)
    board=models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)

class Posts(models.Model):
    message=models.TextField(max_length=2555)
    topic=models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)