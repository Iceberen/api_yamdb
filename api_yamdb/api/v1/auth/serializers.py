from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


    def validate(self, attrs):
        instance = User(**attrs)
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.args[0])
        return attrs
