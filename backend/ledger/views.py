from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AccountSerializer


# Create your views here.
# this a view to get all accounts by the current user
class AccountCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format='json'):
        user_id = request.user.id
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
