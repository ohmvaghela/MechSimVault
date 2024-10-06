from django.shortcuts import render
from .models import SubComments
from .serializers import SubCommentSerializer
from apps.userComments.models import Comments
from apps.simulations.models import Simulation
from apps.siteUser.models import SiteUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class getSubComments(APIView):
  def get(self,request):
    subComments = SubComments.objects.all()
    serializer = SubCommentSerializer(subComments,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
 
class getSubCommentById(APIView):
  def get(self,request,pk):
    comment = Comments.objects.get(pk=pk)
    subComments = SubComments.objects.filter(comment_id=comment)
    serializer = SubCommentSerializer(subComments,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

class createSubComment(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes=[IsAuthenticated]
  
  def post(self,request,pk):
    user_id = request.user.id
    try:
      comment = Comments.objects.get(pk=pk)
    except:
      return Response("comment not found",status=status.HTTP_404_NOT_FOUND)
    comment_id  = comment.id
    
    if 'message' not in request.data or len(request.data['message']) == 0:
      return Response("Message of 0 len or not found",status=status.HTTP_400_BAD_REQUEST)
      
    data = request.data.copy()    
    data['user_id'] = user_id
    data['comment_id'] = comment_id
    
    serializer = SubCommentSerializer(data=data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class deleteSubComment(APIView):
  authentication_classes=[JWTAuthentication]
  permission_classes=[IsAuthenticated]
  
  def delete(self,request,pk):
    user = request.user
    try:
      subcomment = SubComments.objects.get(pk=pk)
    except:
      return Response("comment not found",status=status.HTTP_404_NOT_FOUND)
    
    if subcomment.user_id.id != user.id:
      return Response("subcomment not created by this user",status=status.HTTP_404_NOT_FOUND)
    
    subcomment.delete()
    return Response("subcomment deleted successfully",status=status.HTTP_200_OK)
    
    