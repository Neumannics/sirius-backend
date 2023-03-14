from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest
from .models import Class, Notice, Event
from authorization.models import Membership, Permission, Role
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from sirius.utils.perm import has_perm
from sirius.utils.console_context import get_console_data
from django.shortcuts import get_object_or_404
from teams.models import Team
from signup.models import UserSignUp
from rest_framework import serializers

class ClassCreate(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ['team_id']
        model = Class
    def create(self, validated_data):
        instance = Team.objects.get(id = self.context['team_pk'])
        return Class.objects.create(**validated_data,team_id = instance)

class NoticeCreate(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ['team_id']
        model = Notice
    def create(self, validated_data):
        team = Team.objects.get(id = self.context['team_pk'])
        # user = UserSignUp.objects.get
        return Notice.objects.create(**validated_data,team_id = team)
#have to remove the option of choosing the user nad make changes in the backend.

class EventCreate(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ['team_id']
        model = Event
    def create(self, validated_data):
        instance = Team.objects.get(id = self.context['team_pk'])
        return Event.objects.create(**validated_data,team_id = instance)