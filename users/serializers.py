from rest_framework import generics, permissions
from rest_framework import serializers
from .models import User

from django.contrib.auth import get_user_model
User = get_user_model()


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email' ,'role')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password' , 'last_name' , 'first_name' ,'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(self.validated_data ['username'],  
        self.validated_data['email'], self.validated_data['password']  , self.validated_data['last_name'], self.validated_data['first_name'] ,role=validated_data['role'])

        return user

# Change Password
from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)