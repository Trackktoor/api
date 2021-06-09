from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('Name', 'TaskType', 'ProjectType', 'ShortTask', 'Description', 'ProjectLink', 'Photos', 'id')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class NewProjectRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProjectRequest
        fields = ('Name', 'Phone', 'Email', 'Comment', 'ProjectType', 'ProjectTheme', 'ProjectStatus')

    def create(self, validated_data):
        return NewProjectRequest(**validated_data)

class NewConsultRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewConsultRequest
        fields = ('Phone', 'Comment')

    def create(self, validated_data):
        return NewConsultRequest(**validated_data)
