from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Task
from core.serializer import TaskSerializer


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsManager(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'manager']


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'manager', 'employee']
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()

    serializer_class = TaskSerializer


permission_classes = [IsAuthenticated]