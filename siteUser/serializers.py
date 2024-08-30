from rest_framework import serializers
from .models import SiteUser
from django.contrib.auth import authenticate

class SiteUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = SiteUser
    fields = [
        'id', 'profile_picture', 'email', 'is_superuser', 'full_name', 
        'bio', 'institution', 'role', 'country', 'contact_info', 
        'skills', 'signup_date'
    ]
    read_only_fields = ['id', 'signup_date']

class SiteUserCreateSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = SiteUser
    fields = [
        'id','profile_picture', 'email', 'password', 'full_name', 
        'bio', 'institution', 'role', 'country', 'contact_info', 
        'skills'
    ]

  def create(self, validated_data):
    
    user = SiteUser.objects.create_user(
      email=validated_data['email'],
      password=validated_data['password'],
      profile_picture=validated_data.get('profile_picture', 'profile_picture/base.jpg'),
      full_name=validated_data.get('full_name', 'Default name'),
      bio=validated_data.get('bio', ''),
      institution=validated_data.get('institution', ''),
      role=validated_data.get('role', ''),
      country=validated_data.get('country', 'INDIA'),
      contact_info=validated_data.get('contact_info', ''),
      skills=validated_data.get('skills', '')
    )
    
    return user
  
class SiteUserLoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
    email = data.get('email')
    password = data.get('password')

    if email and password:
      user = authenticate(request=self.context.get('request'), email=email, password=password)
      if not user:
        raise serializers.ValidationError("Invalid login credentials")
    else:
      raise serializers.ValidationError("Must include 'email' and 'password'")

    data['user'] = user
    return data

class SiteUserUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = SiteUser
    fields = [
        'profile_picture', 'full_name', 'bio', 'institution', 
        'role', 'country', 'contact_info', 'skills'
    ]
    read_only_fields = ['id', 'signup_date']
