from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Comments
from .serializers import CommentSerializer
from apps.siteUser.models import SiteUser
from apps.simulations.models import Simulation

class GetComments(APIView):
  def get(self, request):
    data = Comments.objects.all()
    serializer = CommentSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class GetCommentsBySim(APIView):
  def get(self, request, pk):
    try:
      sim = Simulation.objects.get(pk=pk)
    except Simulation.DoesNotExist:
      return Response({"error": "Simulation not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
      return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    try:
      data = Comments.objects.filter(simulation=sim).order_by('-date')
    except Exception as e:
      return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    try:
      serializer = CommentSerializer(data, many=True)
    except Exception as e:
      return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.data, status=status.HTTP_200_OK)
            
class CreateComment(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  def post(self, request, pk):
    try:
      sim = Simulation.objects.get(pk=pk)
    except Simulation.DoesNotExist:
      return Response({"message": "Simulation not found"}, status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    if 'message' not in request.data or len(request.data['message']) == 0:
      return Response(
        {"message": "Message of zero length or does not exist"},
        status=status.HTTP_400_BAD_REQUEST
      )
    
    data = request.data.copy()
    data['user'] = user.id
    data['simulation'] = sim.id
    
    serializer = CommentSerializer(
      data=data,
    )
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteComment(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  def delete(self, request, pk):
    user = request.user
    try:
      comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
      return Response({"message": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
    if user.id != comment.user.id:
      return Response({"message": "Only creator of comment can delete comment"}, status=status.HTTP_400_BAD_REQUEST)
      
    comment.delete()
    return Response("comment deleted succesfully",status=status.HTTP_204_NO_CONTENT)
