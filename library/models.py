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


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    issue_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выдачи')
    return_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата возврата')

    def __str__(self):
        return f"{self.book.name} - {self.user.full_name}"

    class Meta:
        verbose_name = 'Выдача книги'
        verbose_name_plural = 'Выдача книг'
