from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES=(
    ('CR','curd'),
    ('ML','milk'),
    ('Ls','lassi'),
    ('Ms','Milkshake'),
    ('PN','panner'),
    ('GN','Ghee'),
    ('Ch','cheese'),
    ('ice','icecream'),

)
STATE_CHOICES=(
    ('Andaman & nichobar Island','Andaman & nichobar Island'),
    ('Arunachal pradesh','Arunachal pradesh'),
    ('Asam','Asam'),
    ('Andrha Pradesh','Andrha Pradesh'),
    ('Bihar','Bihar'),
    ('chatisgrah','chatisgrah'),
    ('Goa','Goa'),
    ('gurjarat','gujarat'),
    ('hariyana','hariyana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Maharshtra','Mahrastra'),
    ('utterpradesh','utterpradesh'),
    ('utrakhand','utrakhand'),



)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    comopstion=models.TextField(default="")
    pradapp=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.name
    

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    Zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
        

     
