#from django.shortcuts import render
from django.http.response import  HttpResponse

# Create your views here.

def myIndex(request):
    my_name =  request.POST.get('name',"CGU")
    return HttpResponse("Hello "+my_name)
