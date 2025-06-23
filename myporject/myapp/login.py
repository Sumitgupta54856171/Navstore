from .models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import customer

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = User.objects.filter(email=email, password=password)
        
        if user:
            email = request.POST['email']
            request.session[email] = email
            response = redirect('home')
            response.set_cookie(
                key='e-com',
                value=email,
                secure=True,
                httponly=True,
                max_age=60*60*24 
            )
            return response
        else:
            return HttpResponse('Invalid username or password')
    return render(request, 'login.html')
def logout(request):
    if request.method == 'POST':
        request.COOKIES.delete('e-com')
        request.session.flush()
        return redirect('/')
def deleteproduct(request):
    if request.method == 'POST':
        productid = request.POST['productid']
        customer.objects.filter(productid=productid).delete()
        return redirect('/')