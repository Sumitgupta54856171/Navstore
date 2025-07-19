from django import forms
from .models import User,transaction,addcart
from rest_framework import serializers
class Userform(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["username","email","password"]
class Transactionform(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields=["user","productid","quantity","price","total","orderid","transactionid","success"]
class Addcartform(serializers.ModelSerializer):
    class Meta:
        model = addcart
        fields=["user","productid"]
