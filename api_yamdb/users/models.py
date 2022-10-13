from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_USER = 'user'
ROLE_ADMIN = 'admin'
ROLE_MODERATOR = 'moderator'

ROLE_CHOICES = (
    (ROLE_USER, 'Пользователь'),
    (ROLE_MODERATOR, 'Модератор'),
    (ROLE_ADMIN, 'Администратор'),
)


class CustomUser(AbstractUser):
    """Описание полей модели CustomUser наследуемой от AbstractUser."""

    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        verbose_name='Логин'
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        verbose_name='Адрес электронной почты'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='О себе'
    )
    role = models.CharField(
        max_length=255,
        choices=ROLE_CHOICES,
        default=ROLE_USER,
        verbose_name='Роль'
    )

    @property
    def is_user(self):
        return self.role == ROLE_USER

    @property
    def is_admin(self):
        return self.role == ROLE_ADMIN

    @property
    def is_moderator(self):
        return self.role == ROLE_MODERATOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
