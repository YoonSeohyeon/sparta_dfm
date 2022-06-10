from unittest import result
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import permissions
# Create your views here.
class CustomPermission(permissions.BasePermission):
    """
    Allow any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permission_rank > 5)
        return 


class UserApiView(APIView):
    permission_classes = [CustomPermission]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]
    def get(self, request):
        return Response({"message": "get success"})
