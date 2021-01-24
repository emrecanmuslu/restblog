from django.urls import path
from post.api.views import PostListAPIView, PostDetailAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView

app_name = 'posts'
urlpatterns = [
    path('list/', PostListAPIView.as_view(), name='list'),
    path('detail/<int:id>/', PostDetailAPIView.as_view(), name='detail'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('edit/<int:id>/', PostUpdateAPIView.as_view(), name='update'),
    path('delete/<int:id>/', PostDeleteAPIView.as_view(), name='delete'),
]
