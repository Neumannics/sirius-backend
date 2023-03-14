from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics,response,status
from .serializers import *
from .models import Team
from django.http import JsonResponse
from authorization.models import *
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
        
    

    
class AcceptJoin(generics.RetrieveUpdateAPIView):
    serializer_class=AcceptRequestSerializer
    queryset=JoinRequest.objects.all()

    def put(self, request, *args, **kwargs):
        instance = JoinRequest.objects.get(pk=self.kwargs['pk'])
        # print(instance)
        instance.status='A'
        instance.save()
        membership = Membership.objects.filter(team_id=instance.team_id, user_id=instance.user_id).first()
        if not membership:
            membership = Membership(team_id=instance.team_id, user_id=instance.user_id, )
            role = Role.objects.filter(team_id=instance.team_id, role_name='Member').first()
            membership.role_id = role
            membership.save()
        return response.Response(status=status.HTTP_200_OK)
    
class DeclineRequest(generics.RetrieveUpdateAPIView):
    serializer_class=AcceptRequestSerializer
    queryset=JoinRequest.objects.all()

    def put(self, request, *args, **kwargs):
        instance = JoinRequest.objects.get(pk=self.kwargs['pk'])
        print(instance)
        instance.status='R'
        instance.save()
        return response.Response(status=status.HTTP_200_OK)

class RequestedList(generics.ListCreateAPIView):
    serializer_class = RequestTeamSerializer
    queryset = JoinRequest.objects.all()

class RequestJoinDetail(generics.ListAPIView):
    serializer_class=RequestTeamSerializer
    queryset=JoinRequest.objects.all()
    def get_queryset(self):
         return super().get_queryset().filter(team_id=self.kwargs['pk'])

class AcceptInvite(generics.RetrieveUpdateAPIView):
    serializer_class = AcceptInvite
    queryset=Invite.objects.all()
    
    def put(self, request, *args, **kwargs):
        # serializer = AcceptInvite
        # if not serializer.is_valid():
        #     return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        # else:
        instance = Invite.objects.get(id=self.kwargs['pk'])
        print(instance)
        instance.status='A'
        instance.save()
        membership = Membership(team_id=instance.team_id, user_id=instance.invited)
        membership.save()
        # print('!!!!!!')

        return response.Response(status=status.HTTP_200_OK)

class InviteList(generics.ListCreateAPIView):
    serializer_class = InviteTeamSerializer
    queryset = Invite.objects.all()

class InviteDetail(generics.ListAPIView):
    serializer_class = InviteTeamSerializer
    queryset = Invite.objects.all()
    def get_queryset(self):
         return super().get_queryset().filter(team_id=self.kwargs['pk'])

class DeclineInvite(generics.RetrieveUpdateAPIView):
    serializer_class = AcceptInvite
    queryset=Invite.objects.all()
    
    def put(self, request, *args, **kwargs):
        
        instance = Invite.objects.get(id=self.kwargs['pk'])
        print(instance)
        instance.status='R'
        instance.save()
        return response.Response(status=status.HTTP_200_OK)


class LeaveTeam(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

class TeamDelete(generics.RetrieveUpdateAPIView):
    serializer_class = RegisterTeamSerializer
    queryset=Team.objects.all()
    def put(self, request, *args, **kwargs):
        team = Team.objects.get(id=kwargs['pk'])
        team.delete()
        return response.Response(status=status.HTTP_200_OK)