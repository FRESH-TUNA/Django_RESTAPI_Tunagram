from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status, viewsets
from post.models import Post
from account.models import User
from post.serializer import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from post.paginator import PostPaginator
import logging
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def retrieve(self, request, pk, format=None):
        serializer = PostDetailSerializer(Post.objects.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        posts = Post.objects.all()
        paginator = PostPaginator()
        result = paginator.paginate_queryset(posts, request)
        serializer = PostListSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PostCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=User.objects.get(email='root@gmail.com'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = PostCreateUpdateSerializer(Post.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk=None):
        serializer = PostCreateUpdateSerializer(Post.objects.get(pk=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
