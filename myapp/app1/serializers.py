from rest_framework import serializers
from .models import User, RefCode, Ref


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RefCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCode
        fields = '__all__'


class RefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ref
        fields = '__all__'
