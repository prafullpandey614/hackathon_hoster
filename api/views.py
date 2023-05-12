from typing import List
from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hackathon, Profile, Submission
from django.contrib.auth.models import User
from .serializers import HackathonSerializer, HackthonParticipantSerializer, ProfileSerializer, SubmissionSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import HackathonParticipant
from django.shortcuts import get_object_or_404
from django.http import Http404
# from rest_framework_simplejwt.views import ObtainJSONWebToken
from django.contrib.auth import login,authenticate

from api import serializers
# Create your views here.

class APIOverview(APIView):
    def get(self,request):
        response= {
            "Register" : "/register",
            "Login" : "/login",
            "Host a Hackathon" : "/host-hackathon",
            "Register in a Hackathon" : "/participate-hackathon",
            "Submit your Solution" : "/submit-solution",
            "My Participation" : "/my-registrations",
            "My Submissions" :"/my-submissions",
        }
        return Response(response)

class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = Profile.objects.create(user=user)
            token = RefreshToken.for_user(user=user)
            response_data = {
                'user': serializer.data,
                'access':str( token.access_token),
                'refresh' : str(token)
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HostHackathonAPIView(CreateAPIView):
    queryset = Hackathon.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HackathonSerializer
    def perform_create(self, serializer):
        user = Profile.objects.get(user=self.request.user)
        serializer.save(organizer=user)

class PartcipantHackathonAPIView(CreateAPIView):
    queryset = HackathonParticipant.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HackthonParticipantSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        hackathon_id = self.request.data.get('hackathon')
        context['hackathon'] = get_object_or_404(Hackathon, pk=hackathon_id)
        return context
    
    def perform_create(self, serializer):
        hackathon = self.get_serializer_context()['hackathon']
        
        participant = Profile.objects.get(user=self.request.user)
        serializer.save(participant=participant, hackathon=hackathon)

class SubmitYourSolutionAPIView(CreateAPIView):
    queryset = Submission.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SubmissionSerializer
    def perform_create(self, serializer):
        print("Running this view function")
        
        participant = Profile.objects.get(user=self.request.user)
        hackathon_id = self.request.data.get('hackathon')
        if not HackathonParticipant.objects.filter(hackathon=hackathon_id,participant=participant):
            raise serializers.ValidationError("You are not registered for this event !")
        serializer.save(participant=participant)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        hackathon_id = self.request.data.get('hackathon')
        context['hackathon'] = get_object_or_404(Hackathon, pk=hackathon_id)
        return context
    
class MyRegistrationsAPIView(ListAPIView):
    queryset = HackathonParticipant.objects.all()
    serializer_class = HackthonParticipantSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user_profile = Profile.objects.get(user = self.request.user)
        queryset = HackathonParticipant.objects.filter(participant=user_profile)
        return queryset    

class MySubmissionAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SubmissionSerializer
    def  get_queryset(self):
        hackathon_id = self.request.query_params.get('id')
        if hackathon_id is None:
            raise Http404
        user_profile = Profile.objects.get(user=self.request.user)
        try:
            submission = Submission.objects.filter(hackathon__id=hackathon_id, participant=user_profile)
        except Submission.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, submission)
        return submission