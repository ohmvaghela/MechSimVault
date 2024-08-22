from rest_framework import serializers
from .models import SubComments

class SubCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = SubComments
    fields = '__all__'
  
  def create(self,validated_data):
    user_id = validated_data.pop('user_id')
    comment_id = validated_data.pop('comment_id')
    subcomment = SubComments.objects.create(
      user_id = user_id,
      comment_id = comment_id,
      **validated_data
    )
    return subcomment