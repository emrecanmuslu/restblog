from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from account.api.serializers import UserSerializer


class ProfileUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj
