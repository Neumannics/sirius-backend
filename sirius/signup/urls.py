from django.urls import path
from .views import UsersListAPI,RegisterUserAPIView,UserDetailAPIView

urlpatterns = [
  path("get-details/",UsersListAPI.as_view()),
  path('register/',RegisterUserAPIView.as_view()),
  path('get-details/<int:pk>/',UserDetailAPIView.as_view()),
]