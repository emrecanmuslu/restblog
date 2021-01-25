from django.urls import path
from comment.api.views import CommentCreateAPIView, CommentListAPIView, CommentUpdateAPIView, CommentDeleteAPIView

app_name = 'comment'
urlpatterns = [
    path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('list/', CommentListAPIView.as_view(), name='list'),
    path('update/<int:id>/', CommentUpdateAPIView.as_view(), name='update'),
    path('delete/<int:id>/', CommentDeleteAPIView.as_view(), name='delete'),
]
