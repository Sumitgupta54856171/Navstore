from .models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = User.objects.filter(email=email, password=password)
        
        if user:
           
            request.session['user_email'] = request.POST['email']
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