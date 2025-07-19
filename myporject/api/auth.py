from django.shortcuts import HttpResponse
from .models import User
from .form import Userform
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
class Auth(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
       try:
          print(request.data)
          form = Userform(data=request.data)
          print(form)
          print("form is valid",form.is_valid())
          if form.is_valid():
             print("form is valid")
             user = form.save()
             try:
                response = Response('User created successfully')
                return response
             except Exception as e:
                return Response(f'Error creating user: {str(e)}')
       except Exception as e:
          return Response(f'Error creating user: {str(e)}')
class Login(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
       try:
          email = request.data.get('email')
          password = request.data.get('password')
          print(email)
          print(password)
          user = User.objects.get(email=email, password=password)
          print(user,"user")
          if user:
            refresh = RefreshToken.for_user(email)
            access = str(refresh.access_token)
            
            isauthenticated = True
            response = Response('Login successful')
            response.set_cookie('email', email)
            response.set_cookie('refresh', refresh)
            response.set_cookie('access', access)
            response.set_cookie('isauthenticated', isauthenticated)
            return response
          else:
             return Response('Invalid credentials')
       except Exception as e:
          return Response(f'Error logging in: {str(e)}')
class Verify(APIView):
    def get(self,request):
        try:
            email = request.COOKIES.get('email')
            refresh = request.COOKIES.get('refresh')
            access = request.COOKIES.get('access')
            if email and refresh and access:
                return Response('User is authenticated')
            else:
                return Response('User is not authenticated')
        except Exception as e:
            return Response(f'Error verifying user: {str(e)}')