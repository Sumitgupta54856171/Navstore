from .models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse , JsonResponse
from .models import customer




def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            print(email)
            print(password)
            user = User.objects.filter(email=email, password=password)
            print(user,"show the detail of user of postgresql fetch data")
            print('user is successfull match')
        
            if user:
                response = JsonResponse({
                "status": "success",
                "message": "User successfully logged in",
                 "email":email,
               })
                request.session[email] = email
            
                response.set_cookie(
                key='e-com',
                value=email,
                secure=True,
                httponly=True,
                max_age=60*60*24 
            )
                return response
            else:
                return JsonResponse({'message': 'Invalid username or password'})
        except Exception as e:
            return JsonResponse({'message': str(e)})
    return render(request, 'login.html')
def logout(request):
    if request.method == 'POST':
        request.COOKIES.delete('e-com')
        request.session.flush()
        return redirect('/')
