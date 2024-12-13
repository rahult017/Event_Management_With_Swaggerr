from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):

    @swagger_auto_schema(
        request_body=None,
        responses={200: 'Logout successful', 400: 'Bad request'}
    )
    def post(self, request):
        try:
            # Invalidate the token by deleting it from the blacklist
            token = request.data.get('refresh')
            if not token:
                return Response({"detail": "Token is required."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # You can use a blacklist app to blacklist the token
                refresh_token = RefreshToken(token)
                refresh_token.blacklist()
                return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
