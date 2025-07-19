from django.urls import path 
from api.auth import Auth,Login,Verify
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
   path('login', Login.as_view(), name='login'),
   path('signup', Auth.as_view(), name='signup'),
   path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
   path('verify', Verify.as_view(), name='verify'),
]
