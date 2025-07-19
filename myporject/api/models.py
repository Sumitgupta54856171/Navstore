from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    class Meta:
        app_label = 'api'
        db_table = 'api_user'
class transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productid = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
    orderid = models.CharField(max_length=500)
    transactionid = models.CharField(max_length=500)
    success = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    class Meta:
        app_label = 'api'
        db_table = 'api_transaction'
class addcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productid = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    class Meta:
        app_label = 'api'
        db_table = 'api_addcart'