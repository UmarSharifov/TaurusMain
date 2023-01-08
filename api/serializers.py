from rest_framework import serializers

from blog.models import *


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

    def create(self, validated_data):
        validated_data['category'] = Category.objects.get(name=validated_data['category'])
        validated_data['user'] = User.objects.get(username='tesla')
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.save()
        return instance
