from django.shortcuts import redirect, render
import uuid
from .models import customer
import logging
logger = logging.getLogger(__name__)
def Additems(request):
    if request.method == "POST":
        productid = uuid.uuid4()
        productname = request.POST.get('productname')
        productprice = request.POST.get('productprice')
        productquantity = request.POST.get('productquantity')
        productdescription = request.POST.get('productdescription')
        productbrand = request.POST.get('productbrand')
        productcolor = request.POST.get('productcolor')
        productmaterial = request.POST.get('productmaterial')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        email = request.COOKIES.get('e-com')
        
        customers = customer(productid=productid, productname=productname, productprice=productprice, productquantity=productquantity, productdescription=productdescription, productbrand=productbrand, productcolor=productcolor, productmaterial=productmaterial, category=category, image=image, email=email)
        customers.save()
        return redirect('/')
               
    return render(request, 'Add.html')


