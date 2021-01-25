from rest_framework import serializers
from post.models import Post


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='posts:detail',
        lookup_field='id'
    )

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'url'
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'user',
            'username',
            'created_at'
        ]

    def get_username(self, obj):
        return str(obj.user.username)


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'user',
            'created_at'
        ]
