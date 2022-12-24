from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from .models import UserSignUp
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import BasePermission,SAFE_METHODS

# Class based view to Get User Details using Token Authentication
class UsersListAPI(generics.ListCreateAPIView):
  permission_classes = (AllowAny,)
  queryset = UserSignUp.objects.all()
  serializer_class=UserSerializer


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


class PostUserWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        

        if request.method in SAFE_METHODS:
            return True
        return obj==request.user

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=[PostUserWritePermission]
  queryset = UserSignUp.objects.all()
  serializer_class = UserSerializer
