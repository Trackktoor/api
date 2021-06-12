from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ('name', 'project_type', 'short_task', 'description', 'project_link', 'photos', 'id')

    def create(self, validated_data):
        return project.objects.create(**validated_data)

class NewProjectRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = new_project_request
        fields = ('name', 'phone', 'email', 'comment', 'project_type', 'project_theme', 'status')

    def create(self, validated_data):
        return new_project_request(**validated_data)

class NewConsultRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = new_consult_request
        fields = ('phone', 'comment')

    def create(self, validated_data):
        return new_consult_request(**validated_data)
