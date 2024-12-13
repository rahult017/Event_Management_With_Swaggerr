import os, sys
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import OutstandingToken
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class LogoutView(APIView):

    @swagger_auto_schema(
        request_body=None,
        responses={200: 'Logout successful', 400: 'Bad request'}
    )
    def post(self, request):
        try:
            user = request.user
            if user.deleted_at:
                print("User account is deleted")
                return Response(status=status.HTTP_200_OK)

            outstanding_tokens = OutstandingToken.objects.filter(user=user)
            if not outstanding_tokens:
                
                return Response(status=status.HTTP_204_NO_CONTENT)

            blacklisted_count = 0
            for token in outstanding_tokens:
                try:
                    refresh_token = RefreshToken(token.token)
                    if not BlacklistedToken.objects.filter(
                        token__jti=refresh_token["jti"]
                    ).exists():
                        refresh_token.blacklist()
                        blacklisted_count += 1
                    else:
                        print("Token already blacklisted: %s", token.token)
                except (InvalidToken, TokenError) as e:
                    print("Skipping token  due to error: %s", e)

            print("User logged out, %d tokens blacklisted.", blacklisted_count)
            logout(request)
            return Response(
                status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(
                "An error of type {} occurred in file {} at line number {}: {}".format(
                    exc_type.__name__, fname, exc_tb.tb_lineno, exc_obj
                )
            )

            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
