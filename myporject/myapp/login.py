from.models import User
from django.shortcuts import redirect,render
from django.http import HttpResponse
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password)
        
        
        if user:
            return redirect('home')
        else:
            return HttpResponse('Invalid username or password')
    return render(request, 'login.html')