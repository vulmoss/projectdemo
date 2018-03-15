from django.shortcuts import render
from block.models import Block
#from django.db import models
#from django.http import HttpResponse



def index(request):
    block_infos = Block.objects.all().order_by("-id")
    return render(request,"index.html",{"blocks":block_infos})




#    return HttpResponse("Hello World")

def artive(request):
    return render(request,"artive.html")
