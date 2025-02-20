from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.db.utils import IntegrityError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.auth.serializers import SignupSerializer, TokenSerializer
from api.v1.auth.utils import send_confirmation_email, get_access_tokens_for_user

User = get_user_model()


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                confirmation_code = default_token_generator.make_token(user)
                send_confirmation_email(confirmation_code=confirmation_code, email=user.email)

                context = {
                    'email': user.email,
                    'username': user.username,
                }

                return Response(context, status=HTTPStatus.OK)
            except IntegrityError:
                return Response(
                    {"error": "Ошибка базы данных. Попробуйте снова."},
                    status=HTTPStatus.INTERNAL_SERVER_ERROR
                )

        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


class TokenView(APIView):
    def post(self, request):

        serializer = TokenSerializer(data=request.data)

        if serializer.is_valid():

            confirmation_code = serializer.validated_data['confirmation_code']
            username = serializer.validated_data['username']

            if not confirmation_code or not username:
                return Response(
                    {'field_name': f'{confirmation_code}'},
                    status=HTTPStatus.BAD_REQUEST
                )

            user = get_object_or_404(User, username=username)
            check_code = default_token_generator.check_token(user, confirmation_code)


            if check_code:
                access_token = get_access_tokens_for_user(user)
                return Response({'token': f'{access_token}'},)

        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
