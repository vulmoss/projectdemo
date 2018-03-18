from django.shortcuts import render
from block.models import Block
#from django.db import models
#from django.http import HttpResponse

#LANGUAGE_CODE='zh-hans'


def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
    return render(request,"article_list.html",{"articles":articles_objs,"b":block})
                                                      
