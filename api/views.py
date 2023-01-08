from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import *
from .serializers import *


class PostAPIView(APIView):

    def get(self, request):
        w = Post.objects.all()
        return Response(
            {'post': PostSerializer(w, many=True).data}
        )

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Post.objects.create(
            title=request.data['title'],
            slug=request.data['slug'],
            content=request.data['content'],
            user=User.objects.get(username='tesla'),
            category=Category.objects.get(name=request.data['category'])
        )
        return Response(
            {"post": PostSerializer(post_new).data}
        )