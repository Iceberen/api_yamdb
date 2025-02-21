from django.conf import settings
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken


def send_confirmation_email(confirmation_code: str, email: str) -> None:
    """Отправляет код подтверждения на почту."""

    subject = 'Ваш код подтверждения'
    message = f'{subject}: {confirmation_code}'

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.ADMIN_EMAIL,
        recipient_list=[email],
    )


def get_access_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return str(refresh.access_token)
