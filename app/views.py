from django.db.models import Count
from django.shortcuts import render
from django.shortcuts import HttpResponse 
from django.views import View
from urllib import request
from .models import Product

# Create your views here.
def first(request):
    return render(request,"app/home.html")

class  Categoriview(View):
    def get(self,request,val):
        product= Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request,"app/category.html",locals())

class ProductDetial(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/Productdetail.html",locals())

    
def  register(request):
    return render(request,"app/signup.html")

def login(request):
    return render(request,"app/signin.html")
    


