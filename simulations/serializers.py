from rest_framework import serializers
from .models import Simulation

class SimulationSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Simulation
    fields = '__all__'
  
  def create(self,validated_data):
    user = self.context['request'].user
    print("user_found :",user)
    simulation = Simulation.objects.create(
      user_id=user,
      title=validated_data.get('title','empty title'),
      description=validated_data.get('description','empty description'),
      Softwares=validated_data.get('Softwares','now expertise'),
      simulation_image=validated_data.get('simulation_image','simulations/default_photo.png'),
      zip_file=validated_data.get('zip_file',None),
      zip_photos=validated_data.get('zip_photos',None),
    )    
    return simulation

class SimulationUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Simulation
    fields = '__all__'
    read_only_fields = ['user_id']