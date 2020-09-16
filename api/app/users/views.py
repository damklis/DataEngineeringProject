from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from users.serializers import UserSerializer, AuthTokenSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    permission_classes = ()


class ObtainTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    permission_classes = ()

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
