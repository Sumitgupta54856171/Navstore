from django.shortcuts import render
from .models import customer
from django.http import HttpResponse
def home(request):
    if request.method == 'GET':
      email = request.COOKIES.get('e-com')
      customers = customer.objects.filter(email=email)
      return render(request, 'home.html',{'email': email,'customers': customers})
    return render(request, 'home.html')