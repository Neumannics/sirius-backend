from django.shortcuts import render
from rest_framework import generics,response,status
from rest_framework.views import APIView
from .serializers import *
from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from sirius.utils.perm import *

# Create your views here.

class CreateRole(generics.ListCreateAPIView):
    serializer_class = CreateRoleSerializer
    queryset = Role.objects.all()
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'team_pk':kwargs['team_pk']})
        serializer.is_valid()
        self.perform_create(serializer)
        return response.Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        return super().get_queryset().filter(team_id = self.kwargs['team_pk'])

class UpdateRoles(APIView):
    # serializer_class = CreateRoleSerializer
    # queryset = Role.objects.all()


    #Also make sure that the role that u are giving is already created for the same team.

    def post(self,request,*args, **kwargs):
        print(request.POST.items())
        for key, role_id in request.POST.items():
            print('!!!!!!!')
            if key.startswith('role-'):
                member_pk = key.split('-')[1]
                membership = Membership.objects.get(pk=member_pk)
                membership.role_id = Role.objects.get(pk=role_id,team_id = kwargs['team_pk'])
                membership.save()
        return response.Response(status=status.HTTP_201_CREATED)
    
    # def get(self,request,*args, **kwargs):
    #     roles = Role.objects.filter(team_id = kwargs['team_pk'])
    #     for role in roles:
    #         print(role)
    #     return response.Response(status=status.HTTP_200_OK)

    # def put(self,request,*args, **kwargs):
    #     for key, role_id in request.POST.items():
    #         print('!!!!!!!!!!!!!!!!!!')
    #         if key.startswith('role-'):
    #             member_pk = key.split('-')[1]
    #             membership = Membership.objects.get(pk=member_pk)
    #             membership.role_id = Role.objects.get(pk=role_id)
    #             membership.save()
    #     return response.Response(status=status.HTTP_201_CREATED)

class UpdateRole(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreateRoleSerializer
    queryset = Role.objects.all()
    def get_queryset(self):
        return super().get_queryset().filter(pk=self.kwargs['pk'],team_id = self.kwargs['team_pk'])
    def put(self, request, *args, **kwargs):
        role = Role.objects.get(pk=kwargs['pk'])
        if str(role.team_id.id) != str(kwargs['team_pk']):
            return HttpResponseBadRequest('Invalid request')
        if not role:
            return HttpResponseBadRequest('Invalid request')
        return response.Response(status=status.HTTP_201_CREATED)    


class UpdatePermissions(generics.RetrieveUpdateAPIView):
    serializer_class = PermissionsSerializer
    queryset = Permission.objects.all()
    def put(self, request, *args, **kwargs):
        if not has_perm('U', 'R', request.user, self.kwargs['team_pk']):
            return HttpResponseForbidden()
        role_pk = request.POST['role-pk']
        perm_string = request.POST['perm-string']
        if not perm_string or not role_pk:
            return HttpResponseBadRequest('Invalid request')
        role = Role.objects.get(pk=role_pk)
        if not role:
            return HttpResponseBadRequest('Invalid request')
        if str(role.team_id.id) != str(self.kwargs['team_pk']):
            return HttpResponseBadRequest('Invalid request')
        role.permissions = perm_string
        role.save()

class ShowPermissions(generics.ListAPIView):
    queryset=Permission.objects.all()
    serializer_class = PermissionsSerializer

class ShowMemberships(generics.ListAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    def get_queryset(self):
        return super().get_queryset().filter(team_id = self.kwargs['team_pk'])



#Didnt understand Permissions properly.
#Didnt implement has_perm entirely in teams app and rest.

    




