from django import forms
from .models import customer 
from .models import User
class customerform(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['productid', 'productname', 'productprice', 'productquantity', 'productimageid', 'productdescription', 'productcategory', 'productbrand','productrate']
class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']        