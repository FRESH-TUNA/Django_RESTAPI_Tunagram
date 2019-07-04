from rest_framework import serializers
from comment.models import Comment
from account.serializer import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField()  
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user','post')
    