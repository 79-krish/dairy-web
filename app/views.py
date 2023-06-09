from django.db.models import Count
from django.shortcuts import render
from django.shortcuts import HttpResponse 
from django.views import View 
from urllib import request
from .models import Product ,Customer
from .forms import CustomerRegistrationForm ,CustomerProfileform
from django.contrib import messages



# Create your views here.
def first(request):
    return render(request,"app/home.html")

def contact(request):
    return render(request,"/contacta.html")

def about(request):
    return render(request,"app/about.html")

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

class  CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return  render(request,"app/customerregestration.html",locals())
    def post(seld,request):
        form=CustomerRegistrationForm(request,POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! user Rgestier Suceesfully ")
        else:
            messages.warning(request,"Invalid Input data")
        return render(request, 'app/cuntomerregestration.html',locals())
    
class profileView(View):
    def get(self,request):
        form=CustomerProfileform()
        return render(request,'app/profile.html',locals())
    def post(self,request):
        return render(request,'app/profile.html',locals())
    


            
    
    

        
    


