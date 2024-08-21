from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import SiteUserSerializer,SiteUserCreateSerializer,SiteUserLoginSerializer,SiteUserUpdateSerializer
from rest_framework.views import APIView
from .models import SiteUser
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class SiteUserList(APIView):
  def get(self,request):
    users = SiteUser.objects.all()
    serializer = SiteUserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class SiteUserCreate(APIView):
  def post(self,request):
    serializer = SiteUserCreateSerializer(data = request.data)
    if serializer.is_valid():
      user = serializer.save()# why save serializer
      refresh = RefreshToken.for_user(user)
      access_token = str(refresh.access_token)
      refresh_token = str(refresh)

      response = Response({
        "message": "User created successfully",
        "user": SiteUserCreateSerializer(user).data,
        "access_token": access_token
      }, status=status.HTTP_201_CREATED)
      
      # Set refresh token in HttpOnly cookie
      response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        httponly=True,
        secure=True,  # Use secure=True in production
        samesite='Strict'
      )
      
      return response

    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)      

class SiteUserLogin(APIView):
  def post(self,request):
    serializer = SiteUserLoginSerializer(data = request.data)
    if serializer.is_valid():
      user = serializer.validated_data['user']
      refresh = RefreshToken.for_user(user)
      access_token = str(refresh.access_token)
      refresh_token = str(refresh)      
      response =  Response({
        "message": "Login successful", 
        "user": user.email,
        "access_token": access_token,
      },
      status=status.HTTP_200_OK)
      response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite='Strict'
      )
      return response
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)      


class SiteUpdateUser(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def post(self,request):
    user = request.user
    if 'email' in request.data or 'password' in request.data:
      return Response({'error': 'Email and password updates are not allowed'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = SiteUserUpdateSerializer(user,data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
class SiteUpdatePassword(APIView):
  authentication_classes=[JWTAuthentication]
  permission_classes=[IsAuthenticated]
  
  def post(self,request):
    
    user = request.user
    
    password = request.data.get('password')
    if password:
      user.set_password(password)
      user.save()
      refresh = RefreshToken.for_user(user)
      access_token = str(refresh.access_token)
      refresh_token = str(refresh)            
      response =  Response({
        "message": "password update successful", 
        "user": user.email,
        "access_token": access_token,
      },
      status=status.HTTP_200_OK)
      response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite='Strict'
      )
      return response
    return Response({"message":"password not found"},status=status.HTTP_400_BAD_REQUEST)
  