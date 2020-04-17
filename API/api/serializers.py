from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Profil, Strangething, Like, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password':{'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ['user','genre','preference','strangething']


class StrangethingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strangething
        fields = ['user', 'title', 'text', 'numb_of_like']


class LikeSerializer(serializers.ModelSerializer):
    strangething = StrangethingSerializer(many=False)
    class Meta:
        model = Like
        fields = ['user', 'strangething']


class CommentSerializer(serializers.ModelSerializer):
    strangething = StrangethingSerializer(many=False)
    class Meta:
        model = Comment
        fields = ['user', 'strangething', 'text']