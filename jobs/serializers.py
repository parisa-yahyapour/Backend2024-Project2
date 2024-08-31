from rest_framework import serializers
from .models import JobPosition

class JobpositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ['position','description','uploaded_date','expiration_date','salary','remote','full_time','part_time','company']
