from rest_framework import serializers
from .models import *

class RegisterTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
    

class RequestTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        fields = '__all__'

class InviteTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ('__all__')
    
class AcceptInvite(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['status']

class AcceptRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        fields = ['status']