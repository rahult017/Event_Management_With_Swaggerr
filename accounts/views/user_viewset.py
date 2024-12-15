from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.serializers.user_serializers import UserSerializer
from events.permissions import IsAdmin

User = get_user_model()

@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_description="Retrieve all users or a specific user",
    responses={200: 'User list retrieved successfully'}
))
@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_description="Create a new user",
    request_body=UserSerializer,
    responses={201: 'User created successfully', 400: 'Validation errors'}
))
class UserListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        users = User.objects.all().exclude(is_superuser=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(
    name='put', 
    decorator=swagger_auto_schema(
        operation_summary="Update an existing user",
        request_body=UserSerializer,
        responses={200: 'User updated successfully', 400: 'Validation errors'}
    )
)
@method_decorator(
    name='delete', 
    decorator=swagger_auto_schema(
        operation_summary="Delete an existing user",
        responses={204: 'User deleted successfully', 404: 'User not found'}
    )
)
@method_decorator(
    name='get', 
    decorator=swagger_auto_schema(
        operation_summary="Retrieve user details",
        responses={200: UserSerializer, 404: 'User not found'}
    )
)
class UserDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
