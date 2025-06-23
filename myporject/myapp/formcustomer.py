from django import forms
from .models import User,customer
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['productname', 'productprice', 'productquantity', 
                 'productdescription', 'productbrand', 
                 'productcolor', 'productmaterial','category','image','email','productid']
class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']       
