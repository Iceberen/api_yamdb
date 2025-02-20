from http import HTTPStatus
from django.db.utils import IntegrityError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.auth.serializers import SignupSerializer
from api.v1.auth.utils import send_confirmation_email


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                send_confirmation_email(username=user.username, email=user.email)

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