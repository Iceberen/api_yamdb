from django.core.exceptions import ValidationError
import re

USERNAME_REGEX = r'^[\w.@+-]+$'


def validate_username(value):
    """Запрещает использовать 'me' в качестве имени пользователя и проверяет допустимые символы."""
    if value.lower() == 'me':
        raise ValidationError('Нельзя использовать "me" в качестве username.')

    if not re.match(USERNAME_REGEX, value):
        raise ValidationError(
            'Имя пользователя содержит недопустимые символы.'
        )

    return value
