from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def frist(request):
    return HttpResponse("it is balck fill it is used to making from creating floder with collection of modules into package")



def second(request):
    return render(request,"frist.html")
