from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


# Create your views here.

class UserCreateApiView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.owner = self.request.user
        new_user.save()


class UserUpdateApiView(generics.UpdateAPIView):
    """Редактирование пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyApiView(generics.DestroyAPIView):
    """Удаление пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
