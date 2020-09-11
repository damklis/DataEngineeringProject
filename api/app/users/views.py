from rest_framework import generics

from users.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

    permission_classes = ()
