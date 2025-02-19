from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('У пользователей должен быть email')
        if not username:
            raise ValueError('У пользователей должен быть username')

        email = self.normalize_email(email)
        extra_fields.setdefault('role', User.Role.USER)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', User.Role.ADMIN)
        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        USER = 'user', 'User'
        MODERATOR = 'moderator', 'Moderator'
        ADMIN = 'admin', 'Admin'

    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=(UnicodeUsernameValidator(),)
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def clean(self):
        if self.username.lower() == "me":
            raise ValidationError({"username": "Имя пользователя не может быть 'me'."})
