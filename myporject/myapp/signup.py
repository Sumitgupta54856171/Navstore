from django.shortcuts import render, redirect
from .formcustomer import userform
from .models import User
from django.http import HttpResponse
from django.utils import timezone

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # Check if user exists first
        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already exists')
        
        form = userform(request.POST)
        if form.is_valid():
            # Add creation timestamp
            user = form.save(commit=False)
            user.createat = timezone.now()
            try:
                user.save()
                return redirect('login')
            except Exception as e:
                return HttpResponse(f'Error creating user: {str(e)}')
        else:
            return render(request, 'signup.html', {'form': form})

    form = userform()
    return render(request, 'signup.html', {'form': form})
       
        

