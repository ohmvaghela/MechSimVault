from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

class VerifyAndRefreshTokenView(APIView):
    def post(self, request, *args, **kwargs):
        access_token = request.data.get('token')
        if not access_token:
            return Response({'error': 'Access token must be provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            AccessToken(access_token)
            return Response({'message': 'Access token is valid'}, status=status.HTTP_200_OK)
        except TokenError:
            # Access token is invalid or expired, try to refresh it
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({'error': 'Refresh token not found in cookies'}, status=status.HTTP_401_UNAUTHORIZED)

            try:
                refresh = RefreshToken(refresh_token)
                new_access_token = refresh.access_token
                return Response({'access': str(new_access_token)}, status=status.HTTP_200_OK)
            except TokenError:
                return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)
