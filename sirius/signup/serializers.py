from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
from .models import UserSignUp
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#used to show data to user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignUp
        fields = ['id','username','email','first_name','last_name','gender']

        
            

#Used for sending data from user to backend
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserSignUp
        fields = ('username', 'password', 'password2',
             'email', 'first_name', 'last_name','gender')
        extra_kwargs = {
          'first_name': {'required': True},
          'last_name': {'required': True}
        }

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = UserSignUp.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


