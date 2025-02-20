from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.v1.validators import validate_username

User = get_user_model()

class SignupSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=(validate_username,)
    )


    def validate(self, attrs):
        """Запрещаем использование email и username, если они принадлежат разным пользователям."""
        email = attrs["email"]
        username = attrs["username"]

        user_with_email = User.objects.filter(email=email).first()
        user_with_username = User.objects.filter(username=username).first()

        if user_with_email and user_with_email.username != username:
            raise serializers.ValidationError({"email": "Этот email уже используется другим пользователем."})

        if user_with_username and user_with_username.email != email:
            raise serializers.ValidationError({"username": "Этот username уже используется другим пользователем."})

        return attrs

    def create(self, validated_data):
        """Создаём пользователя, если его нет, или возвращаем существующего."""
        user, created = User.objects.get_or_create(
            email=validated_data['email'],
            defaults={"username": validated_data['username']}
        )

        return user


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=(validate_username,)
    )
    confirmation_code = serializers.CharField(required=True, write_only=True)
