from itertools import product
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=30)
    createat= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.createat
class customer(models.Model):
    productid = models.IntegerField()
    productname = models.CharField(max_length=30)
    productprice = models.IntegerField()
    productquantity = models.IntegerField()
    productimageid = models.IntegerField(default=0)
    productdescription = models.CharField(max_length=30)
    productcategory = models.CharField(max_length=30)
    productbrand = models.CharField(max_length=30)
    productcolor = models.CharField(max_length=30)
    productmaterial = models.CharField(max_length=30)
    productrate = models.IntegerField()
    
    def __str__(self):
        return self.productname
    
    
class image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_image/')
    def __str__(self):
      return self.name
    @property
    def image_url(self):
        if self.image and hasattr(self.image,'url'):
          return self.imge.url
        return None
