from django.shortcuts import render
from .formcustomer import userform
from .models import User
from django.http import HttpResponse
from django.shortcuts import redirect
def signup(request):
    form = userform()
    email =request.POST.get('email')
    user = User.objects.filter(email=email)
    if user:
        return HttpResponse('Email already exists')
    if request.method == "POST":
      form = userform(request.POST)
      if form.is_valid():
        form.save()
        return redirect('login')
      else:
        return HttpResponse('Invalid username or password')  
        
    return render(request, 'signup.html')
       
        

