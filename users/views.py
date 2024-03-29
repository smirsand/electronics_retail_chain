from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания пользователя.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
