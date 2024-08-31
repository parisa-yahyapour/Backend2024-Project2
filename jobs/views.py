from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobPosition
from .serializers import JobpositionSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class JobPositionList(generics.ListAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobpositionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    