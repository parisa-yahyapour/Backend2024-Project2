from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobPosition, JobRequest
from .serializers import JobpositionSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class JobPositionList(generics.ListAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobpositionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    

class SendRequest(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if not request.user.is_superuser:
            info = request.data
            requested_id = info['requested_job_id']
            job = JobPosition.objects.get(id = requested_id)
            JobRequest.objects.create(requested_job = job, job_seeker_sender = request.user)
            return Response({"applied"})
        else:
            return Response({"failed"})