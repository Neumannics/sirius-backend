from django.shortcuts import render
from rest_framework import generics,response
from .serializers import *
from .models import Team
from django.http import JsonResponse
# Create your views here.

class CreateTeam(generics.ListCreateAPIView):
    serializer_class = RegisterTeamSerializer
    queryset = Team.objects.all()

class TeamView(generics.ListAPIView):
    queryset=Team.objects.all()
    serializer_class = RegisterTeamSerializer
    def get_queryset(self):
        return super().get_queryset().filter(parent_id=self.kwargs['pk'])

# class SendInvite(generics.ListCreateAPIView):
#     serializer_class=InviteTeamSerializer
#     queryset=Invite.objects.all()
#     def post(self, request, *args, **kwargs):
#         if not Invite.objects.filter(status = 'P', team_id=self.kwargs['pk'], invited=self.kwargs['user']).exists():
#                     invite = Invite(team_id=Team.objects.get(id=self.kwargs['pk']), created_by=self.request.user, invited=get_user_model().objects.get(pk=self.kwargs['user']))
#                     invite.save()    
#     def get_queryset(self):
#         return super().get_queryset().filter(invited=self.kwargs['user'])
        
    

class AcceptInvite(generics.ListCreateAPIView):

class RequestedList(generics.ListCreateAPIView):
    serializer_class = RequestTeamSerializer
    queryset = JoinRequest.objects.all()

class RequestJoinDetail(generics.ListAPIView):
    serializer_class=RequestTeamSerializer
    queryset=JoinRequest.objects.all()
    def get_queryset(self):
         return super().get_queryset().filter(team_id=self.kwargs['pk'])

class InviteList(generics.ListCreateAPIView):
    serializer_class = InviteTeamSerializer
    queryset = Invite.objects.all()

class InviteDetail(generics.ListAPIView):
    serializer_class = InviteTeamSerializer
    queryset = Invite.objects.all()
    def get_queryset(self):
         return super().get_queryset().filter(team_id=self.kwargs['pk'])