from django.shortcuts import redirect, render,HttpResponse
import uuid
from .models import customer,User
import logging
logger = logging.getLogger(__name__)
def Additems(request):
    if request.method == "POST":
      try:  
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
        user = User.objects.get(email=email)
        
        
        customers = customer(productid=productid, productname=productname, productprice=productprice, productquantity=productquantity, productdescription=productdescription, productbrand=productbrand, productcolor=productcolor, productmaterial=productmaterial, category=category, image=image, email=user.id)
        customers.save()
        return redirect('/')
      except Exception as e:
        print(e)
        return HttpResponse(f'Error creating user: {str(e)}')               
    return render(request, 'Add.html')


def updateitems(request):
  if request.method == "POST":
    try:
      productid = request.POST.get('productid')
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
      user = User.objects.get(email=email)
      
      customers = customer.objects.get(productid=productid)
      customers.productname = productname
      customers.productprice = productprice
      customers.productquantity = productquantity
      customers.productdescription = productdescription
      customers.productbrand = productbrand
      customers.productcolor = productcolor
      customers.productmaterial = productmaterial
      customers.category = category
      customers.image = image
      customers.email = user.id
      customers.save()
      return redirect('/')
    except Exception as e:
      print(e)
      return HttpResponse(f'Error updating user: {str(e)}')      

def deleteproduct(request):
    if request.method == 'POST':
        productid = request.POST['productid']
        customer.objects.filter(productid=productid).delete()
        return redirect('/')      