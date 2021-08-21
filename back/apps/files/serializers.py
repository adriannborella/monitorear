from rest_framework import serializers

class FileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

class RequestSerializer(serializers.Serializer):    
    token = serializers.CharField(max_length=200)
    # files = FileSerializer(many=True)