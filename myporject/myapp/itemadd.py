from django.shortcuts import redirect, render
from django.contrib import messages
from .models import image
from .formcustomer import CustomerForm, ImageForm  
import uuid
import logging
logger = logging.getLogger(__name__)
def Additems(request):
    if request.method == "POST":
        print('POST request received')
        product_id = str(uuid.uuid4())[:8]
        print(f'Generated product_id: {product_id}')
        name =request.COOKIES.get('e-com')
        print(name,request.FILES)
        image_form = ImageForm(request.POST,request.FILES)
        print(name)
        print(image_form.is_valid())
        form = CustomerForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
               
    return render(request, 'Add.html')

