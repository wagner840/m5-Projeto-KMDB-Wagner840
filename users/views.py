from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.permissions import IsAdminOrReadOnly, IsSelfOrAdmin
from users.serializers import UserSerializer
from rest_framework.permissions import AllowAny


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSelfOrAdmin]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj

