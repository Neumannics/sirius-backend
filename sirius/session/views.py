from django.shortcuts import render
from rest_framework import generics,response,status
from sirius.utils.perm import *
from .models import *
from .serializers import *
# Create your views here.


class CreateClass(generics.ListCreateAPIView):
    serializer_class = ClassCreate
    queryset = Class.objects.all()
    def post(self, request, *args, **kwargs):
        # if not has_perm('C', 'C', request.user, kwargs['pk']):
        #         return HttpResponseForbidden()
        serializer = self.get_serializer(data=request.data,context={'team_pk':kwargs['team_pk']})
        if serializer.is_valid():
            self.perform_create(serializer)
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class UpdateClass(generics.RetrieveUpdateDestroyAPIView):
    serializer_class  = ClassCreate
    queryset = Class.objects.all()


class CreateNotice(generics.ListCreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeCreate
    def post(self, request, *args, **kwargs):
        # if not has_perm('C', 'N', request.user, kwargs['pk']):
        #     return HttpResponseForbidden()
        # print('!!!!!!!!!!!')
        # print(request.user)
        serializer = self.get_serializer(data=request.data,context={'team_pk':kwargs['team_pk'],'user':request.user})
        if serializer.is_valid():
            self.perform_create(serializer)
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class UpdateNotice(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeCreate

class CreateEvent(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class  = EventCreate
    def post(self, request, *args, **kwargs):
        # if not has_perm('C', 'C', request.user, kwargs['pk']):
        #         return HttpResponseForbidden()
        serializer = self.get_serializer(data=request.data,context={'team_pk':kwargs['team_pk']})
        if serializer.is_valid():
            self.perform_create(serializer)
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class UpdateEvent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreate

class timetable(generics.ListAPIView):
    # if not has_perm('R', 'C', request.user, pk):
    #     return HttpResponseForbidden()
    serializer_class = ClassCreate
    queryset = Class.objects.all()
    def get_queryset(self):
        return super().get_queryset().filter(team_id = self.kwargs['pk'])

class notice_board(generics.ListAPIView):
    serializer_class = NoticeCreate
    queryset = Notice.objects.all()
    def get_queryset(self):
        return super().get_queryset().filter(team_id = self.kwargs['pk'])

class Calendar(generics.ListAPIView):
    serializer_class = EventCreate
    queryset = Event.objects.all()
    def get_queryset(self):
        return super().get_queryset().filter(team_id = self.kwargs['pk'])


    
        
        


