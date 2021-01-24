from rest_framework.generics import CreateAPIView, ListAPIView
from comment.api.paginations import CommentPagination
from comment.api.serializers import CommentCreateSerializer, CommentListSerializer
from comment.models import Comment


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        return Comment.objects.filter(parent=None)
