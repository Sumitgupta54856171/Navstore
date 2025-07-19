from django.shortcuts import render
from .models import customer,User
from django.http import HttpResponse
from django.db.models import Q,F
def home(request):
    if request.method == 'GET':
      email = request.COOKIES.get('e-com')
      user = User.objects.get(email=email)
      num = customer.objects.count()
      if num > 0:
          customers = customer.objects.filter(email=user.id)
          return render(request, 'home.html',{'email': email,'customers': customers})
      else:
          user = User.objects.filter(email=email)
          return render(request, 'home.html', {'email': email, 'user': user})
      return render(request,'home.html')     
     
     
    return render(request, 'home.html')