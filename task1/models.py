from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator


class User(AbstractUser):
    uid= models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,unique=True,
    validators=[
        RegexValidator(
            regex='^(a|A).*(0|1)$',
            message='Username must start with a or A and end with 0 or 1',
            code='invalid_username'
        ),
    ])
    join_date= models.DateTimeField(auto_now_add=True,blank=True,null=True)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Assingment(models.Model):
    tid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    task_title = models.CharField(max_length=200,blank=True,null=True,validators=[MinLengthValidator(10)])
    task_description  = models.TextField(blank=True,null=True,max_length=2000)
    task_pic = models.ImageField(upload_to='images',blank=True,null=True)
    create_time_stamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.task_title
