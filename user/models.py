from django.db import models

# Create your models here.

class User(models.Model):
    SEX=(
        ('male','男'),
        ('female','女')
    )
    phonenum = models.CharField(max_length=20,verbose_name='手机号')
    nickname = models.CharField(max_length=32,verbose_name='昵称')
    sex = models.CharField(max_length=20, choices=SEX, verbose_name='性别')
    birth_year = models.IntegerField(default=2000,verbose_name='出生年')
    birth_month = models.IntegerField(default=1,verbose_name='出生月')
    birth_day = models.IntegerField(default=1,verbose_name='手出生日')
    avatar = models.FileField(verbose_name='个人形象')
    location = models.CharField(max_length=50,verbose_name='常居地')