from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from post.models import Post
from account.models import User
from post.serializer import *
from rest_framework.response import Response
from comment.serializer import *
from comment.models import Comment
from rest_framework.pagination import PageNumberPagination
from comment.paginator import CommentPaginator
class CommentListView(APIView):
    def get(self, request, pk, format=None):
        post=Post.objects.get(pk=pk)
        comments = post.all_comments()
        paginator = CommentPaginator()
        result = paginator.paginate_queryset(comments, request)
        serializer = CommentSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = CommentCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=Post.objects.get(pk=pk), user=User.objects.get(email='root@gmail.com'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def patch(self, request, pk, format=None):
        serializer = CommentCreateUpdateSerializer(Comment.objects.get(pk=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response({'comment':'deleted'}, status=status.HTTP_204_NO_CONTENT)