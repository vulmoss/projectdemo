from django.db import models
from block.models import Block
from django import forms
class Article(models.Model):
    block = models.ForeignKey(Block,verbose_name="版块ID")
    title = models.CharField("版块名词",max_length=100)
    content = models.CharField("版块描述",max_length=10000)
    status = models.IntegerField("状态",choices = ((0,"正常"),(-1,"删除")))
    User = models.CharField("作者",max_length=100)
    create_timestamp = models.DateTimeField("创建时间",auto_now_add=True)
    last_update_timestamp = models.DateTimeField("最后更新时间",auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"

class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=0)

"""

class Comment(models.Model):
    objects = CommentManager()
    owner = models.ForeignKey(User, verbose_name="作者")
    article = models.ForeignKey(Article, verbose_name="所属")
    content = models.CharField(u"内容",max_length=10000)

"""


"""
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields = ["title","content"]

"""
