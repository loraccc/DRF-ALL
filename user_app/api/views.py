from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .serializers import UserRegistrationSerializer

from user_app import models


@api_view (['POST', ]) 
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
    return Response({'success': True},status=status.HTTP_200_OK)


@api_view(['POST',])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)

        data={}

        if serializer.is_valid():
            user = serializer.save()
            data['response']="Registration Successfull"
            data['username']=user.username
            data['email']=user.email

            token=Token.objects.get(user=user).key
            data['token']=(token)
        else:
            data=serializer.error_messages

            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(data)
