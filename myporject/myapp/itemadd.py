from django.shortcuts import redirect,render
from models import customer
from formcustomer import customerform

def Additems(request):
    if request.method == "POST":
        form = customerform(request.POST)
        if form.is_valid():
            return home
        
