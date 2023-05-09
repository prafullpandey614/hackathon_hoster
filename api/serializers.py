from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile,Hackathon

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name']

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = "__all__"
        read_only_fields = ["organizer"]