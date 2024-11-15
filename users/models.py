from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='почта',
        unique=True
    )
    phone = models.CharField(
        max_length=55, verbose_name='Телефон',
        blank=True, null=True
    )
    full_name = models.CharField(
        max_length=100,
        verbose_name='ФИО пользователя'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        