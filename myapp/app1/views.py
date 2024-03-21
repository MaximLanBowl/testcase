from django.shortcuts import render
from rest_framework import viewsets
from .models import User, RefCode, Ref
from .serializers import UserSerializer, RefSerializer, RefCodeSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RefCodeView(viewsets.ModelViewSet):
    queryset = RefCode.objects.all()
    serializer_class = RefCodeSerializer


class RefView(viewsets.ModelViewSet):
    queryset = Ref.objects.all()
    serializer_class = RefSerializer

