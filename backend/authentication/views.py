from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import request


from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer

class ObtainTokenPair(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    # this prints the entire request object

    serializer_class = MyTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        username_or_email = request.data.get('username')
        password = request.data.get('password')
        if not username_or_email or not password:
            return Response({'error': 'Please provide both username/email and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user_model = get_user_model()
        user = user_model.objects.get(Q(username__iexact=username_or_email) | Q(email__iexact=username_or_email))

        # Pass the user object to the serializer and also the 'username_or_email' value
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token_response = serializer.validated_data

        # Return the token pair response
        return Response(token_response, status=status.HTTP_200_OK)


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
