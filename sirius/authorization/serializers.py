from rest_framework import serializers
from .models import *


class CreateRoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','role_name','role_description','permissions','team_id']
        read_only_fields = ['team_id']
        model = Role
    def create(self, validated_data):
        # validated_data.pop('team_id')
        instance = Team.objects.get(id=self.context['team_pk'])
        return Role.objects.create(**validated_data,team_id = instance)


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Permission

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Membership

# class PostList(serializers.ModelSerializer):
    

