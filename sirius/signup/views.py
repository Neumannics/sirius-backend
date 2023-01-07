from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from .models import UserSignUp
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics,status
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

# Class based view to Get User Details using Token Authentication


class UsersListAPI(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = UserSignUp.objects.all()
    serializer_class = UserSerializer


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class PostUserWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj == request.user


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserWritePermission,]
    serializer_class = UserSerializer
    
    def get(self, request,pk):
        try:
            user_profile = request.user
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'first_name': user_profile.first_name,
                    'last_name': user_profile.last_name,
                    'gender': user_profile.gender,
                }]
            }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
            }
        return Response(response, status=status_code)
