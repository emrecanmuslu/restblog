from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from post.api.paginations import PostPagination
from post.api.serializer import PostListSerializer, PostDetailSerializer, PostCreateSerializer
from post.models import Post
from post.api.permissions import IsOwner


class PostListAPIView(ListAPIView):
    queryset = Post.objects.select_related('user').all()
    serializer_class = PostListSerializer
    pagination_class = PostPagination


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.select_related('user').all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.select_related('user').all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsOwner]

    def create(self, request, *args, **kwargs):
        pass

    def validate_title(self, value):
        pass


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.select_related('user').all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        pass

    def validate_title(self, value):
        pass


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.select_related('user').all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'
