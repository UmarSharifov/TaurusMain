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
        serializer.save()
        return Response(
            {"post": serializer.data}
        )

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT is not Allowed"})

        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Object is not find"})

        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT is not Allowed"})

        Post.objects.get(pk=pk).delete()

        return Response({"post": "delete post " + str(pk)})