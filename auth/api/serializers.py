from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions

User = get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def _validate_account(self, username, password):
        user = None
        if username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = 'Must include "username" and "password".'
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = None

        if username:
            try:
                user = User.objects.get(username__iexact=username)
            except Exception as e:
                raise exceptions.ValidationError(e)

        user = self._validate_account(username, password)
        if not user:
            raise exceptions.ValidationError({'error': 'Wrong Password!'})
        attrs['user'] = user
        return attrs


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
