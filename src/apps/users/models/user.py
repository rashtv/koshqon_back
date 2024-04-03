from django.contrib.auth.models import (
    AbstractUser,
)
from django.db import models

from apps.users.models.user_manager import UserManager
from apps.common.models.soft_delete_model import SoftDeleteModel


class User(
    AbstractUser,
    SoftDeleteModel
):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-date_joined',)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()
    email = None

    is_staff = models.BooleanField(
        verbose_name='is admin',
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name='is superuser',
        default=False,
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        default='77777777777'
    )

    first_name = models.CharField(
        verbose_name='Имя пользователя',
        max_length=255,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия пользователя',
        max_length=255,
        blank=True,
        null=True,
    )
    password_last_updated = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
