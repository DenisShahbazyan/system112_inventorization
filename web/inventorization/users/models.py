from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель 'Пользователи'."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    username = models.CharField(
        verbose_name='имя пользователя',
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        verbose_name='почта',
        max_length=254,
        unique=True,
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['id']
