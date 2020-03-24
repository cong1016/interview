from django.db import models

# Create your models here.
class Player(models.Model):
    clientid = models.CharField(max_length=20,db_index = True,verbose_name='客户端id')
    grade = models.CharField(max_length=50,verbose_name='玩家分数')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'player'

