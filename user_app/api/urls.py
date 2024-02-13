from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import register_user,logout_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns=[
    
    #LoginLogout
    path('login/',obtain_auth_token,name='login'),
    path('logout/',logout_view,name='logout'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/refresh/', TokenVerifyView.as_view(), name='token_refresh'),


    #User Register
    path('register/',register_user,name='register')
]