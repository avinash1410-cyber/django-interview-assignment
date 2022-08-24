from rest_framework import serializers
from .models import Account,Book
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','id']

class AccountSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Account
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
