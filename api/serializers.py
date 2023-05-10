from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile,Hackathon, HackathonParticipant
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
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
    def create(self, validated_data):
        user = self.context['request'].user
        user = Profile.objects.get(user=user)
        validated_data['organizer'] = user
        return super().create(validated_data)
    
class HackthonParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonParticipant
        fields = "__all__"
        read_only_fields = ["participant"]
    def validate_subimission_file(self,file):
        hackathon  = self.context['hackathon']
        allowed_file_types = []
        if hackathon.type_of_submission=="image":
            allowed_file_types = ['jpg', 'jpeg', 'png']
        elif hackathon.type_of_submission == "file":
            allowed_file_types = ['pdf', 'doc', 'docx']
        elif hackathon.type_of_submission == "link":
            url_validator = URLValidator()
            submission_file = file
            try:
                url_validator(submission_file)
            except :
                raise serializers.ValidationError("Submission file must be a valid URL")
        file_extension = file.name.split('.')[-1]
        if file_extension not in allowed_file_types:
            raise ValidationError(f"Invalid file type. Allowed types are: {','.join(allowed_file_types)}")
        return file
    def create(self, validated_data):
        user = self.context['request'].user
        participant = Profile.objects.get(user=user)
        validated_data['participant'] = participant
        return super().create(validated_data)