from rest_framework import serializers
from .models import Users, Resource



class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'permissions']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 
                  'headline', 'summary', 'profile_picture', 'cover_photo', 
                  'location', 'industry', 'current_position', 'current_company', 
                  'social_media_accounts']

class CreateUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model =Users
        fields = ["username","password"]

class SocialMediaAccountSerializer(serializers.Serializer):
    platform = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    url = serializers.URLField()
