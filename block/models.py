from django.db import models

class Block(models.Model):
    name = models.CharField("版块名称",max_length=100)
    desc = models.CharField("描述",max_length=100)
    manager_name = models.CharField("管理员名字",max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "版块"
        verbose_name_plural = "版块"
