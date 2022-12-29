from django.contrib.auth.models import AbstractUser
from django.db import models


class Departament(models.Model):
    departament_name = models.CharField(
        verbose_name='отдел',
        max_length=150,
    )


class UserRole:
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


CHOICES_ROLE = (
    (UserRole.USER, 'user'),
    (UserRole.MODERATOR, 'moderator'),
    (UserRole.ADMIN, 'admin'),
)


class User(AbstractUser):
    """Модель 'Пользователи'."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    username = models.CharField(
        verbose_name='имя пользователя',
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='почта',
        max_length=254,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=150,
    )
    middle_name = models.CharField(
        verbose_name='отчество',
        max_length=150,
        blank=True,
    )
    departament = models.ForeignKey(
        Departament,
        on_delete=models.PROTECT,
        related_name='user',
        verbose_name='отдел',
        null=True,
    )
    role = models.CharField(
        verbose_name='роль',
        max_length=16,
        choices=CHOICES_ROLE,
        default='user',
    )

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['id']
