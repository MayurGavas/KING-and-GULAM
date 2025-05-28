from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
#from .models import UserProfile


class UserAccountCreateSerialiser(ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        #UserProfile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name')
