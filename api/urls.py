from django.urls import path

from .views import *


urlpatterns = [
    path('v1/postlist', PostAPIView.as_view(), name='PostList')
]
