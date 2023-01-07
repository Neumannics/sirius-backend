from django.urls import path
from .views import *
from django.urls.conf import include

app_name = 'teams'

urlpatterns = [
    path('create/',CreateTeam.as_view()),
    path('<pk>/info',TeamView.as_view()),
    # path('<pk>/send-request/<user>',SendInvite.as_view()),
    path('join-request/',RequestedList.as_view()),
    path('create-invite/',InviteList.as_view()),
    path('<pk>/invites/',InviteDetail.as_view()),
    path('<pk>/join-request/',RequestJoinDetail.as_view()),
]