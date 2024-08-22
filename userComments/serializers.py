from rest_framework import serializers
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
    
    def create(self, validated_data):
        user_id = validated_data.pop('user')
        sim_id = validated_data.pop('simulation')
        comment = Comments.objects.create(
            user=user_id,
            simulation=sim_id,
            **validated_data
        )
        return comment
