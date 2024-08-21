from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import SiteUserSerializer,SiteUserCreateSerializer,SiteUserLoginSerializer
from rest_framework.views import APIView
from .models import SiteUser

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
      return Response({
        "message":"user created succesfully",
        "user":SiteUserCreateSerializer(user).data
      },status.HTTP_202_ACCEPTED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)      

class SiteUserLogin(APIView):
  def post(self,request):
    serializer = SiteUserLoginSerializer(data = request.data)
    if serializer.is_valid():
      user = serializer.validated_data['user']
      return Response({"message": "Login successful", "user": user.email},
                      status=status.HTTP_200_OK)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)      
