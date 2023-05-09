from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hackathon, Profile
from django.contrib.auth.models import User
from .serializers import HackathonSerializer, ProfileSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.views import ObtainJSONWebToken
from django.contrib.auth import login,authenticate
# Create your views here.

class OverviewAPIView(APIView):
    def get(self,request):
        response= {
            "register" : "/register",
            "login" : "/login",
        }
        return Response(response)

class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # profile = Profile.objects.create(user=user)
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
    permission_classes = [IsAuthenticated]
    serializer_class = HackathonSerializer
    