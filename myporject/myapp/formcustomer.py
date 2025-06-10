from django import forms
from .models import User,customer,image
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['productname', 'productprice', 'productquantity', 
                 'productdescription', 'productcategory', 'productbrand', 
                 'productcolor', 'productmaterial', 'productrate']
class ImageForm(forms.ModelForm):
    class Meta:
        model = image
        fields = ['name', 'image']
class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']       
