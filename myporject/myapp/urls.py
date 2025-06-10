from django.urls import path
from . import  home
from . import signup
from . import login
urlpatterns = [
    path('', home.home, name='home'),
    path('signup', signup.signup, name='signup'),
    path('login', login.login, name='login'),
]