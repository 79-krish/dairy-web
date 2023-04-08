from django.db import models

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

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    comopstion=models.TextField(default="")
    pradapp=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    product_image=models.ImageField(upload_to='product')
    def  __str__(self):
        return self.title
    


        

     
