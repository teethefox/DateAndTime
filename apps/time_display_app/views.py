from django.shortcuts import render, HttpResponse,redirect
from time import localtime, strftime
def index(request):
    context = {
    "time": strftime("%m-%d-%Y %I:%M %p %Z", localtime())
    }
    return render(request,'index.html', context)


# Create your views here.
