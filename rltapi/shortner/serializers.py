from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.Serializer):
    full_url = serializers.URLField()
    url_hash_value = serializers.CharField(max_length=16, default='')
    clicks = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(default='')

    def create(self, validated_data):
        return URL.objects.create(**validated_data)


