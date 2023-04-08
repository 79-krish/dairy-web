from django.shortcuts import render
from django.shortcuts import HttpResponse 
from django.views import View
from urllib import request

# Create your views here.
def first(request):
    return render(request,"app/home.html")

class  Categoriview(View):
    def get(self,request,val):
        return render(request,"app/category.html",locals())
    
def  register(request):
    return render(request,"app/signup.html")

def login(request):
    return render(request,"app/signin.html")
    


