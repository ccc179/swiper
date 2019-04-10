import datetime

from django.db import models


# Create your models here.

class User(models.Model):
    SEX = (
        ('male', '男'),
        ('female', '女')
    )
    phonenum = models.CharField(max_length=20, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=32, unique=True, verbose_name='昵称')
    sex = models.CharField(max_length=20, choices=SEX, verbose_name='性别')
    birth_year = models.IntegerField(default=2000, verbose_name='出生年')
    birth_month = models.IntegerField(default=1, verbose_name='出生月')
    birth_day = models.IntegerField(default=1, verbose_name='手出生日')
    avatar = models.CharField(max_length=200, verbose_name='个人形象')
    location = models.CharField(max_length=20, verbose_name='常居地')

    @property
    def age(self):
        # 今天减去用户的生日,取得(delta)相差的日期
        days = datetime.date.today()-datetime.date(self.birth_year,self.birth_month,self.birth_day)
        # 返回年数
        return days.days//365

    def to_string(self):
        return {
            'phonenum':self.phonenum,
            'nickname':self.nickname,
            'sex':self.sex,
            'age':self.age,
            'avatar':self.avatar,
            'location':self.location
        }
