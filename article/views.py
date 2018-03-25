from django.shortcuts import render
from block.models import Block
from django import forms
#from django.db import models
#from django.http import HttpResponse

#LANGUAGE_CODE='zh-hans'


def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    page_no = int(request.GET.get("page_no","1"))
    all_articles = Article.objects.filter(block=block, status = 0).order
    p = Paginator(all_articles,ARTICLES_CNT_1PAGE)
    page = p.page(page_no)
    articles_objs = page.object_list
    page_cnt = p.num_pages
    current_no = page_no
    page_links = [i for i in range(page_no - 5,page_no + 6) if i > 0 and i <= p.num_pages]
    previous_link = page_links[0] -1
    next_link = page_links[-1] + 1
    has_previous = previous_link > 0
    has_next = next_link <= page_cnt
    return render(request,"article_list.html",{"articles":articles_objs,"page_cnt":page_cnt,"current_no":current_no,"page_links":page_links,"previous_link":previous_link,"next_link":next_link,"has_previous":has_previous,"has_next":has_next})

                                                      


if form.is_valid():
    article = form.save(commit=False)
    article.block= block
    article.status=0
    article.save()
    return redirect("/article/list/%s" % block_id)
else:
    return render(request,"article_create.html",{"b":block,"form":form})

