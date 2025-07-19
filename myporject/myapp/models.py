from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=30)
    createat = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
    class Meta:
        app_label = 'myapp'
        db_table = 'myapp_user'
class customer(models.Model):
    productid = models.CharField(max_length=250)
    productname = models.CharField(max_length=250)
    productprice = models.IntegerField()
    productquantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    productdescription = models.CharField(max_length=5000)
    productbrand = models.CharField(max_length=250)
    productcolor = models.CharField(max_length=250)
    productmaterial = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    email = models.ForeignKey(User, on_delete=models.CASCADE)

 
    def __str__(self):
        return self.productname
    class Meta:
        app_label = 'myapp'
        db_table = 'myapp_customer'     

       
  