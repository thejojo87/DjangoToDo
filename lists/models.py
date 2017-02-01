from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    # 一对一，一条信息，对应一个人
    # related_name是反向关联
    belong_to = models.OneToOneField(to=User, related_name='info')

    # 添加要扩展到 User 中的新字段
    age = models.IntegerField("年龄",null=True, blank=True)
    address = models.CharField("地址",max_length=50, null=True, blank=True)

    def __str__(self):
        return self.belong_to

class List(models.Model):

    def get_absolute_url(self):
        return reverse('lists:view_list',args=[self.id])

class Item(models.Model):
    text = models.TextField(max_length=100, default="")
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')


    def __str__(self):
        return self.text