from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 from the data to prevent it from being saved
        email=validated_data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        user = User.objects.create_user(**validated_data)
        return user
