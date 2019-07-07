from rest_framework import serializers
from post.models import Post
from tunagramAuth.serializer import UserSerializer


class PostListSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField()
    getPartOfContent = serializers.ReadOnlyField()  
    class Meta:
        model = Post
        exclude = ('content',)


class PostDetailSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('user',)
    

