from rest_framework import serializers
from .models import *

class RegisterTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id','name','description','parent_id')
    



class RequestTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        fields = '__all__'

class InviteTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ('__all__')