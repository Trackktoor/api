from rest_framework import serializers
from .models import URL, URL_hash

class URLSerializer(serializers.Serializer):
    url = serializers.URLField()
    short_url = serializers.CharField(max_length=16, default='')
    redirects = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(default='')
    def create(self, validated_data):
        return URL.objects.create(**validated_data)




