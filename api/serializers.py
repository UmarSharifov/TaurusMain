from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    content = serializers.CharField()
    photo = serializers.ImageField(read_only=True)
    user = serializers.CharField(read_only=True)
    category = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(read_only=True)
