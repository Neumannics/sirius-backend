from django.urls import path
from .views import *

app_name = 'authorization'

urlpatterns = [
    path('role/create/', CreateRole.as_view()),
    path('role/update/', UpdateRoles.as_view()),
    path('role/<pk>/update/', UpdateRole.as_view()),
    path('permissions/', ShowPermissions.as_view(), name='show_permissions'),
    path('permissions/update/<pk>', UpdatePermissions.as_view(), name='show_permissions'),
    path('memberships/', ShowMemberships.as_view(), name='show_memberships'),

    ]