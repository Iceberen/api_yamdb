from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.auth.serializers import SignupSerializer
from api.v1.auth.utils import generate_confirmation_code, send_confirmation_email


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            send_confirmation_email(username=user.username, email=user.email)

            context = {
                'email': user.email,
                'username': user.username,
            }


            return Response(context, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
