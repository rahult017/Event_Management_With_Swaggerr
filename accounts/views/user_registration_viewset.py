import os, sys

from rest_framework import viewsets, status
from rest_framework.views import APIView

from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny

from accounts.serializers.user_registeration_serializers import UserRegistrationSerializer

from utility.custom_response import create_response
from utility.serializers_errors import serializer_error

class UserRegistrationViewset(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        responses={201: 'User registered successfully', 400: 'Validation errors'}
    )

    def post(self, request):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)