from django.urls import path
from .views import *
urlpatterns = [
    path('class/create/<team_pk>',CreateClass.as_view()),
    path('class/update/<pk>',UpdateClass.as_view()),

    path('notice/create/<team_pk>',CreateNotice.as_view()),
    path('notice/update/<pk>',UpdateNotice.as_view()),
    
    path('event/create/<team_pk>',CreateEvent.as_view()),
    path('event/update/<pk>',UpdateEvent.as_view()),

    path('calendar/<pk>',Calendar.as_view()),
    path('notice_board/<pk>',notice_board.as_view()),
    path('time_table/<pk>',timetable.as_view()),
]
