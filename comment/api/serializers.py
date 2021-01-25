from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.models import Comment
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError('something went wrong')

        return attrs


class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'replies',
            'post',
            'user'
        ]

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content'
        ]
