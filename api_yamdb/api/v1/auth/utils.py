import hashlib
import hmac
import base64
from django.conf import settings
from django.core.mail import send_mail

LENGTH_CONFIRMATION_CODE = 12


def generate_confirmation_code(username: str, email: str) -> str:
    """Генерирует код подтверждения."""

    hash_data = f"{username}{email}".encode()
    key = settings.SECRET_KEY.encode()

    hmac_hash = hmac.new(key, hash_data, hashlib.sha512).digest()

    return base64.urlsafe_b64encode(hmac_hash).decode()[:LENGTH_CONFIRMATION_CODE]


def send_confirmation_email(username: str, email: str) -> None:
    """Отправляет код подтверждения на почту."""

    code = generate_confirmation_code(username=username, email=email)
    subject = 'Ваш код подтверждения'
    message = f'{subject}: {code}'

    send_mail(
        subject=subject, message=message,
        from_email=settings.ADMIN_EMAIL, recipient_list=[email]
    )

def verify_confirmation_code(username: str, email: str, code: str) -> bool:
    """Сверяет код."""
    expected_code = generate_confirmation_code(username=username, email=email)
    return hmac.compare_digest(expected_code, code)
