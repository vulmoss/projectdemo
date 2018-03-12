from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    return render(request,"index.html")




#    return HttpResponse("Hello World")

def artive(request):
    return render(request,"artive.html")
