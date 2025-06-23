from django.urls import path
from . import  home
from . import signup
from . import login
from . import itemadd

urlpatterns = [
    path('', home.home, name='home'),
    path('signup', signup.signup, name='signup'),
    path('login', login.login, name='login'),
    path('addproduct', itemadd.Additems, name='add-product'),
    path('logout', login.logout, name='logout'),
    path('deleteproduct', login.deleteproduct, name='delete-product'),
] 