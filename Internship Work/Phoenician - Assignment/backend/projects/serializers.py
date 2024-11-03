from rest_framework import serializers
from .models import Project, ProjectDetail

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetail
        fields = ['title', 'items']

class ProjectSerializer(serializers.ModelSerializer):
    details = ProjectDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'details']
