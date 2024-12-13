import sys,os
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from accounts.serializers.user_login_serializers import UserLoginSeriaizer

from utility.serializers_errors import serializer_error

User = get_user_model()

class LoginView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        request_body=UserLoginSeriaizer,
        responses={200: 'Login successful', 400: 'Invalid credentials'}
    )
    def post(self, request):
        try:
            serializer = UserLoginSeriaizer(data=request.data)
            if serializer.is_valid():
                try:
                    user = User.objects.get(email=serializer.validated_data["email"])
                except User.DoesNotExist:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST)
                except User.MultipleObjectsReturned:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST)

                if user.deleted_at:
                    return Response(
                        status=status.HTTP_200_OK)

                # create token
                user_token = RefreshToken.for_user(user)

                # return token
                token_data = {
                    "access": str(user_token.access_token),
                    "refresh": str(user_token),
                }
                return Response(token_data,status=status.HTTP_200_OK)
            elif not serializer.is_valid():
                return Response(serializer_error(serializer._errors),status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(
                "An error of type {} occurred in file {} at line number {}: {}".format(
                    exc_type.__name__, fname, exc_tb.tb_lineno, exc_obj
                )
            )
            return Response(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)
