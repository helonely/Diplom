from django.db import models

from users.models import User


class Author(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Полное имя автора книги',
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название книги'
    )

    availability = models.BooleanField(
        verbose_name='Наличие книги'
    )

    genre = models.CharField(
        max_length=100,
        verbose_name='Жанр книги'
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь',
        blank=True, null=True
    )

    author = models.ForeignKey(
        Author, on_delete=models.CASCADE,
        verbose_name='Автор книги'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
