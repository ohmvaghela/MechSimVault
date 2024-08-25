from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Simulation
from .serializers import SimulationSerializer,SimulationUpdateSerializer,LikesSerializer
from siteUser.models import SiteUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Simulation,Likes
from .serializers import SimulationSerializer


class GetSims(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            sims = Simulation.objects.all()
            serializer = SimulationSerializer(sims, many=True)
            sims_data = serializer.data

            for sim in sims_data:
                sim_id = sim['id']
                try:
                    likes_count = Likes.objects.filter(sim_id=sim_id).count()
                    sim['likes'] = likes_count
                except Likes.DoesNotExist:
                    sim['likes'] = 0

            return Response(sims_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GetSimsByID(APIView):
    def get(self, request, pk):
        try:
            user = SiteUser.objects.get(pk=pk)
            sims = Simulation.objects.filter(user_id=user)
            serializer = SimulationSerializer(sims, many=True)
            sims_data = serializer.data

            for sim in sims_data:
                sim_id = sim['id']
                try:
                    likes_count = Likes.objects.filter(sim_id=sim_id).count()
                    sim['likes'] = likes_count
                except Likes.DoesNotExist:
                    sim['likes'] = 0

            return Response(sims_data, status=status.HTTP_200_OK)
        except SiteUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddLike(APIView):
    def post(self, request, user_id, sim_id):
        data = {
            'user_id': user_id,
            'sim_id': sim_id
        }

        serializer = LikesSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class GetSimBySimId(APIView):
    def get(self, request, pk):
        try:
            simulation = Simulation.objects.get(pk=pk)
            serializer = SimulationSerializer(simulation)
            sim_data = serializer.data

            try:
                likes_count = Likes.objects.filter(sim_id=simulation.id).count()
                sim_data['likes'] = likes_count
            except Likes.DoesNotExist:
                sim_data['likes'] = 0

            return Response(sim_data, status=status.HTTP_200_OK)
        except Simulation.DoesNotExist:
            return Response({"error": "Simulation not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddSimulation(APIView):
  authentication_classes=[JWTAuthentication]
  permission_classes=[IsAuthenticated]
  
  def post(self, request):    
    user = request.user
    request.data['user_id'] = user.id

    if 'zip_file' not in request.data or 'zip_photos' not in request.data:
      return Response(
        {"message":"zip file or zip photo does not exist"},
        status=status.HTTP_400_BAD_REQUEST
      )
    
    serializer = SimulationSerializer(
        data=request.data, 
        context={'request': request})
    
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  

class UpdateSimulation(APIView):
  
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  def post(self, request,pk):
    data = request.data.copy()
    try:
        simulation = Simulation.objects.get(pk=pk)
    except Simulation.DoesNotExist:
        return Response({"error": "Simulation not found"}, status=status.HTTP_404_NOT_FOUND)
      
    if simulation.user_id.id != request.user.id:
      return Response({"ids":f"user_id:{request.user.id}, sim:{simulation.user_id.id}","error": "user cannot update others model"}, status=status.HTTP_401_UNAUTHORIZED)
    
    data['user_id'] = simulation.user_id.id
     
    # Handle zip_file separately
    if 'zip_file' in request.FILES:
        simulation.delete_zip_file()
    # Handle zip_photos separately
    if 'zip_photos' in request.FILES:
      simulation.delete_zip_photos()
    # Handle simulation_image separately
    if 'simulation_image' in request.FILES:
      simulation.delete_simulation_image()
        
    serialize = SimulationUpdateSerializer(
      simulation,data=data,
      context={'request':request},
      partial=True
    )
    
    if serialize.is_valid():
      serialize.save()
      return Response({
        "message": "Simulation updated", 
        "title": serialize.data['title'],
        "description":serialize.data['description']
        },status=status.HTTP_202_ACCEPTED)
    
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteSimulation(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  
  def post(self, request,pk):
    user = request.user
    
    try:
      sim = Simulation.objects.get(pk=pk)
    except Simulation.DoesNotExist:
      return Response({"error": "Simulation not found"}, status=status.HTTP_404_NOT_FOUND)
    
    
    if user.id != sim.user_id.id:
      return Response({"ids":f"user_id:{user.id}, sim:{sim.user_id.id}","error": "user cannot delete others model"}, status=status.HTTP_401_UNAUTHORIZED)
    
    sim.delete()
    return Response({
      "message": "deleted successfully", 
      },status=status.HTTP_200_OK)


