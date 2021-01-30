from django.urls import path, include

from account.api.views import ProfileUpdateAPIView

app_name = 'account'
urlpatterns = [
    path('profile/', ProfileUpdateAPIView.as_view(), name='profile')
]